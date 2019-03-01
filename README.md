**Quick links:** [COMPAS](https://compas-dev.github.io) | [COMPAS main repo](https://github.com/compas-dev/compas) | [COMPAS main docs](https://compas-dev.github.io/main/)

# Workshop: COMPAS introduction

COMPAS introduction workshop for the new Cluster of Excellence *"Integrative Computational Design and Construction for Architecture (IntCDC)"*

## Schedule

* 

---

## Requirements

* Operating System: Mac (OSX), Windows
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.x
* Rhino 5.0/6.0
* Code editor: Sublime Text 3
* Git: [official command-line client](https://git-scm.com/) or visual GUI (e.g. [Github Desktop](https://desktop.github.com/) or [SourceTree](https://www.sourcetreeapp.com/))

<details><summary><i>Rhino 5.0</i></summary>
If you use Rhino 5.0, make sure to install the following

* [Grasshopper](https://www.grasshopper3d.com/)
* [GHPython](https://www.food4rhino.com/app/ghpython)
* [IronPython 2.7.5](https://github.com/IronLanguages/main/releases/tag/ipy-2.7.5) ([see here for details about this manual update](https://compas-dev.github.io/main/environments/rhino.html#ironpython-1)).

</details>

## Getting started

We will install **COMPAS** using Anaconda.
Anaconda uses *environments* to create isolated spaces to manage the various dependencies and requirements of different projects.
It is recommended that you make a new environment specifically for the workshop.

**1. Clone the workshop repository.**

You have two options.

<details><summary><i>a. Using a visual git client (e.g. SourceTree)</i></summary>

* Go to "File -> Clone / New"
* Select "Clone from URL"
* Provide the source URL: `https://github.com/BlockResearchGroup/WS_cluster.git`
* Provide a destination path (i.e. the folder where you wish to place all workshop material)

</details>

<details><summary><i>b. Using git command line client</i></summary>

* On Windows: launch the Anaconda Prompt
* On Mac: launch the Terminal
* Go to the destination folder where you wish to place all the workshop material
* Run `git clone https://github.com/BlockResearchGroup/WS_cluster.git`

</details><br />

**2. Create an environment and install COMPAS.**

* On Windows: launch the Anaconda prompt (**run as administrator**)
* On Mac: launch the Terminal

Go to the repository folder you just cloned and do

```bash
conda env create -f workshop.yml
conda activate workshop
```

<details><summary><i>Not working?</i></summary>

Make sure you really changed into the repository folder.
For example, if you cloned the repository into a folder called `Code` in your home directory,
you should type:

* On Mac: ```cd ~/Code/WS_cluster```
* On Windows: ```cd %USERPROFILE%\Code\WS_cluster```

</details><br />

**3. Check your installation**

* On Windows: type `python` in the Anaconda prompt
* On Mac: type `python` in the Terminal

```python
>>> import compas
>>> import compas_rhino
>>> import compas_ghpython
```

If no error messages appear, you're good to go!

**4. Configure Rhino**

**5. Set up your development environment**

---

## Exercises

---

## Troubleshooting
