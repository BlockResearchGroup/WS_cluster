**Quick links:** [COMPAS](https://compas-dev.github.io) | [COMPAS main repo](https://github.com/compas-dev/compas) | [COMPAS main docs](https://compas-dev.github.io/main/)

# Workshop: COMPAS introduction

COMPAS introduction workshop for the new Cluster of Excellence *"Integrative Computational Design and Construction for Architecture (IntCDC)"*

---

## Schedule

*   Day 1
    *   10.00: Introduction by Philipe
    *   10.30: COMPAS intro
    *   11.30: Discussion & Questions
    *   12.00: Installation & Setup
    *   12.30: Lunch
    *   13.30: COMPAS packages
    *   14.00: compas_fofin
    *   16.00: compas_fea
*   Day 2
    *   09.00: Recap & Questions
    *   10.00: COMPAS for robotics (tentative)
    *   11.00: compas_fab
    *   12.00: Lunch
    *   13.00: COMPAS projects
    *   14.00: Hackathon

*"COMPAS intro"* is a presentation about the COMPAS ecosystem during which we will
run various code snippets to get familiar with the design principles and basic
functionality of the main library.

*"COMPAS packages"* gives an overview of the currently available research and extension
packages and of the package development procedures.

In *"compas_fofin"* we will develop a (dummy) form finding package using the cookiecutter
template for COMPAS packages.

*"compas_fea"* is a demo of the Finite Element Analysis package for COMPAS,
and *"compas_fab"* is a demo of the ROS interface.
For more info, see [FEA workshop]() and [Robotic Assembly workshop](), respectively.

---

## Requirements

* Operating System: Mac (OSX), Windows
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.x
* [Rhino 5.0/6.0](https://www.rhino3d.com/)
* Code editor: Whatever you normally work with for Python coding.
  Otherwise, we recommend [Sublime Text]() or [VS Code]().
* Git: [official command-line client](https://git-scm.com/) or visual GUI (e.g. [Github Desktop](https://desktop.github.com/) or [SourceTree](https://www.sourcetreeapp.com/))

<details><summary><i>Rhino 5.0</i></summary>
If you use Rhino 5.0, make sure to install the following

* [Grasshopper](https://www.grasshopper3d.com/)
* [GHPython](https://www.food4rhino.com/app/ghpython)
* [IronPython 2.7.5](https://github.com/IronLanguages/main/releases/tag/ipy-2.7.5) ([see here for details about this manual update](https://compas-dev.github.io/main/environments/rhino.html#ironpython-1)).

</details>

---

## Getting started

We will install **COMPAS** using *conda*, the package manager of Anaconda.
Anaconda uses *environments* to create isolated spaces to manage the various dependencies and requirements of different projects.
It is recommended that you make a new environment specifically for the workshop.

**1. Clone the workshop repository.**

You have two options.

<i>a. Using a visual git client (e.g. SourceTree)</i>

* Launch SourceTree
* Go to `File -> Clone / New`
* Select `Clone from URL`
* Provide the source URL: `https://github.com/BlockResearchGroup/WS_cluster.git`
* Provide a destination path (i.e. the folder where you wish to place all workshop material)

<i>b. Using the git command line client</i>

* *On Windows*: launch the Anaconda Prompt
  <br />*On Mac*: launch the Terminal
* Go to the destination folder where you wish to place all the workshop material
* Run `git clone https://github.com/BlockResearchGroup/WS_cluster.git`

**2. Create an environment and install COMPAS.**

* *On Windows*: launch the Anaconda prompt (**run as administrator!**)
  <br />*On Mac*: launch the Terminal

Go to the repository folder you just cloned and run

```bash
conda env create -f workshop.yml
conda activate workshop
```

<details><summary><i>Not working?</i></summary>

Make sure you really are in the repository folder.
For example, if you cloned the repository into a folder called `Code` in your home directory,
you should type:

*On Mac*: ```cd ~/Code/WS_cluster```
<br />*On Windows*: ```cd %USERPROFILE%\Code\WS_cluster```

before running the *conda* commands listed above.

</details>

**3. Check your installation**

*On Windows*: type `python` in the Anaconda prompt
<br />*On Mac*: type `python` in the Terminal

```python
>>> import compas
>>> import compas_rhino
>>> import compas_ghpython
```

If no error messages appear, you're good to go!
Type `exit()` to quit the interactive Python session.

The packages `compas`, `compas_rhino`, `compas_ghpython` (and `compas_blender`) are
now installed in your environment, and will be available in Python if the environment
is active.

**4. Configure Rhino**

To make the installed Python packages of the COMPAS main library available in Rhino,
run the following from the Anaconda Prompt (Windows) or the Terminal (Mac):

```bash

```

**5. Set up your development environment**

---

## Exercises

---

## Troubleshooting
