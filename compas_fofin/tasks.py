from __future__ import print_function

import contextlib
import glob
import os
import sys
from shutil import rmtree

from invoke import Exit
from invoke import task

try:
    input = raw_input
except NameError:
    pass


HERE = os.path.dirname(__file__)


class Log(object):

    def __init__(self, out=sys.stdout, err=sys.stderr):
        self.out = out
        self.err = err

    def flush(self):
        self.out.flush()
        self.err.flush()

    def write(self, message):
        self.flush()
        self.out.write(message + '\n')
        self.out.flush()

    def info(self, message):
        self.write('[INFO] %s' % message)

    def warn(self, message):
        self.write('[WARN] %s' % message)


log = Log()


def confirm(question):
    while True:
        response = input(question).lower().strip()
        if not response or response in ('n', 'no'):
            return False
        if response in ('y', 'yes'):
            return True
        print('Focus, kid! It is either (y)es or (n)o', file=sys.stderr)


@task(default=True)
def help(ctx):
    ctx.run('invoke --list')
    log.write('Use "invoke -h <taskname>" to get detailed help for a task.')


@task(help={'docs': 'True to clean up generated documentation, otherwise False',
            'bytecode': 'True to clean up compiled python files, otherwise False.',
            'builds': 'True to clean up build/packaging artifacts, otherwise False.'})
def clean(ctx, docs=True, bytecode=True, builds=True):
    if builds:
        ctx.run('python setup.py clean')
    if bytecode:
        for root, dirs, files in os.walk(HERE):
            for f in files:
                if f.endswith('.pyc'):
                    os.remove(os.path.join(root, f))
            if '.git' in dirs:
                dirs.remove('.git')
    folders = []
    if docs:
        folders.append('docs')
        folders.append('docsource/api/generated')
    folders.append('dist/')
    if bytecode:
        folders.append('src/compas_fofin/__pycache__')
    if builds:
        folders.append('build/')
        folders.append('src/compas_fofin.egg-info')
    for folder in folders:
        rmtree(os.path.join(HERE, folder), ignore_errors=True)


@task(help={
      'rebuild': 'True to clean all previously built docs before starting, otherwise False.',
      'doctest': 'True to run doctests, otherwise False.',
      'check_links': 'True to check all web links in docs for validity, otherwise False.'})
def docs(ctx, doctest=False, rebuild=True, check_links=False):
    if rebuild:
        clean(ctx)
    if doctest:
        ctx.run('sphinx-build -b doctest docsource docs')
    ctx.run('sphinx-build -b html docsource docs')
    if check_links:
        ctx.run('sphinx-build -b linkcheck docsource docs')


@task()
def check(ctx):
    log.write('Checking MANIFEST.in...')
    ctx.run('check-manifest')
    log.write('Checking metadata...')
    ctx.run('python setup.py check --strict --metadata')
    # log.write('Running flake8 python linter...')
    # ctx.run('flake8 src tests setup.py')
    # log.write('Checking python imports...')
    # ctx.run('isort --check-only --diff --recursive src tests setup.py')


@task(help={
      'checks': 'True to run all checks before testing, otherwise False.'})
def test(ctx, checks=False, doctest=False):
    if checks:
        check(ctx)
    cmd = ['pytest']
    if doctest:
        cmd.append('--doctest-modules')
    ctx.run(' '.join(cmd))


@task(help={
      'release_type': 'Type of release follows semver rules. Must be one of: major, minor, patch.'})
def release(ctx, release_type):
    if release_type not in ('patch', 'minor', 'major'):
        raise Exit('The release type parameter is invalid.\nMust be one of: major, minor, patch')
    ctx.run('invoke check test')
    ctx.run('bumpversion %s --verbose' % release_type)
    ctx.run('python setup.py clean --all sdist bdist_wheel')
    if confirm('You are about to upload the release to pypi.org. Are you sure? [y/N]'):
        files = ['dist/*.whl', 'dist/*.gz', 'dist/*.zip']
        dist_files = ' '.join([pattern for f in files for pattern in glob.glob(f)])
        if len(dist_files):
            ctx.run('twine upload --skip-existing %s' % dist_files)
        else:
            raise Exit('No files found to release')
    else:
        raise Exit('Aborted release')
