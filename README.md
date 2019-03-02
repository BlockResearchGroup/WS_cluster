[COMPAS](https://compas-dev.github.io) | [COMPAS main repo](https://github.com/compas-dev/compas) | [COMPAS main docs](https://compas-dev.github.io/main/)

# Workshop: COMPAS introduction

COMPAS introduction workshop for the new Cluster of Excellence *"Integrative Computational Design and Construction for Architecture (IntCDC)"*

## Schedule

*   Day 1
    *   10.00: Introduction by Philipe
    *   10.30: COMPAS framework -- *Presentation about the structure of COMPAS*
    *   11.00: Discussion & Questions
    *   11.30: Installation & Setup
    *   12.00: Lunch
    *   13.00: COMPAS main -- *Overview of the main library and example snippets of core functionality*
    *   13.45: COMPAS packages -- *Overview of available add-on packages*
    *   14.00: compas_fofin -- *Development of a basic form finding package use a COMPAS cookiecutter*
    *   16.00: compas_fea -- *Demo of the Finite Element Analysis package by Andrew Liew (BRG)*
*   Day 2
    *   09.00: Recap & Questions
    *   10.00: COMPAS for robotic assembly -- *Example snippets for working with robots and assemblies*
    *   11.00: compas_fab -- *Demo of the ROS interface by Romana Rust (GKR)*
    *   12.00: Lunch
    *   13.00: COMPAS projects -- *Overview of collaborative projects (with industry) managed through COMPAS*
    *   14.00: Hackathon -- *Work on your own project*

## Requirements

* Operating System: Mac (OSX) or Windows
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.x
* [Rhino](https://www.rhino3d.com/)
* Code editor: We recommend [Sublime Text](https://www.sublimetext.com/) for this workshop.
* Git: [official command-line client](https://git-scm.com/) or visual GUI (e.g. [Github Desktop](https://desktop.github.com/) or [SourceTree](https://www.sourcetreeapp.com/))

> **Note**
>
> If you use Rhino 5.0, make sure to install the following
> 
> * [Grasshopper](https://www.grasshopper3d.com/)
> * [GHPython](https://www.food4rhino.com/app/ghpython)
> * [IronPython 2.7.5](https://github.com/IronLanguages/main/releases/tag/ipy-2.7.5)
    ([see here for details about this manual update](https://compas-dev.github.io/main/environments/rhino.html#ironpython-1)).

## Getting started

We will install **COMPAS** using *conda*, the package manager of Anaconda.
Anaconda uses *environments* to create isolated spaces to manage the various dependencies and requirements of different projects.
We will install **COMPAS** and its dependencies in a new environment specifically for the workshop.

**1. Clone the workshop repository.**

<i>a. Using a visual git client (e.g. SourceTree)</i>

* Launch SourceTree
* Go to `File -> Clone / New`
* Select `Clone from URL`
* Provide the source URL: `https://github.com/BlockResearchGroup/WS_cluster.git`
* Provide a destination path (i.e. the folder where you wish to place all workshop material)

<i>b. Using the git command line client</i>

* *On Windows*: launch Anaconda Prompt, **as administrator!**
  <br />*On Mac*: launch Terminal
* Go to the destination folder where you wish to place all the workshop material
* Run `git clone https://github.com/BlockResearchGroup/WS_cluster.git`

**2. Create an environment and install COMPAS.**

If you haven't done so yet, 
launch Anaconda Prompt **as administrator!** (*on Windows*)
or Terminal (*on Mac*).

Go to the repository folder you just cloned and run

```bash
conda env create -f workshop.yml
conda activate workshop
```

> **Not working?**
>
> Make sure you really are in the repository folder, before running the commands above.
> For example, if you cloned the repository into a folder called `Code` in your home directory,
> you should run the following to change to the correct folder:
>
> *On Mac*: ```cd ~/Code/WS_cluster```
> <br />*On Windows*: ```cd %USERPROFILE%\Code\WS_cluster```

**3. Check the installation**

Launch the Python interpreter and import `compas`, `compas_rhino`, `compas_ghpython`.

*On Windows*: type `python` in Anaconda Prompt
<br />*On Mac*: type `python` in Terminal

```python
>>> import compas
>>> import compas_rhino
>>> import compas_ghpython
```

If no error messages appear, you're good to go.
Type `exit()` to quit the interpreter.

The packages `compas`, `compas_rhino`, `compas_ghpython` (and `compas_blender`) are
now installed in your environment, and will be available in Python if the environment
is active.

**4. Configure Rhino**

To make the installed packages available in Rhino,
run the following from Anaconda Prompt (*on Windows*) or Terminal (*on Mac*):

```bash
python -m compas_rhino.install -v 5.0 -p compas compas_rhino compas_ghpython
```

> **Note** (Windows only)
>
> Use `-v 6.0` instead of `-v 5.0` if you want to use Rhino 6 instead of Rhino 5.

Open Rhino and run the script [verify_rhino.py](verify_rhino.py).
If this does not throw an error and prints the correct COMPAS version (`0.4.10`),
Rhino is properly configured.

> **Note**
>
> To run a script in Rhino, just type `RunPythonScript` at the Rhino command prompt
> and select the script you want to run.

**5. Set up your development environment**

You can use any development environment that you're comfortable with,
but the instructions for this workshop are written for [Sublime Text](https://www.sublimetext.com/).
Detailed instructions for installing and configuring Sublime Text can be found [here](https://compas-dev.github.io/main/environments/sublimetext.html).

Once Sublime Text is set up, open an new window and add the workshop folder to a new project

```
Sublime Text: Project > Add Folder to Project...
```

The folder and its contents should appear in the sidebar.
Select *Conda* as Build System, activate the workshop environment,
and Run the script [verify_editor.py](verify_editor.py).
If this does not throw an error and prints the correct COMPAS version (`0.4.10`),
your editor is properly configured.

## Examples

*   Network
    *   shortest path (plot): [network_shortestpath.py](examples/network_shortestpath.py)
    *   shortest path (interactive plot): [network_shortestpath.py](examples/network_shortestpath.py)
    *   equilibrium (dynamic plot): [network_equilibrium.py](examples/network_equilibrium.py)
*   Mesh
    *   dijkstra path (Rhino): [mesh_dijkstra_rhino.py](examples/mesh_dijkstra_rhino.py)
    *   equilibrium (Rhino): [mesh_equilibrium_rhino.py](examples/mesh_equilibrium_rhino.py)
    *   smoothing on surface (Rhino): [mesh_smoothing_rhino.py](examples/mesh_smoothing_rhino.py)
    *   subdivision (Rhino): [mesh_subdivision_rhino.py](examples/mesh_subdividion_rhino.py)
    *   isolines (plot): [mesh_isolines.py](examples/mesh_isolines.py)
    *   planarisation (plot): [mesh_planarization.py](examples/mesh_planarization.py) 
