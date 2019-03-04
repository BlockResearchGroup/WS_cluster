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
* [Anaconda Python Distribution](https://www.anaconda.com/download/): 3.7
* [Rhino](https://www.rhino3d.com/)
* Code editor: We recommend [VS Code](https://code.visualstudio.com/) for this workshop.
* Git: [official command-line client](https://git-scm.com/)

> **Note**
>
> If you use Rhino 5.0 on Windows, make sure to install the following
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

* On Windows: launch Anaconda Prompt (**as administrator**)
  <br />On Mac: launch Terminal
* Go to the destination folder where you wish to place all the workshop material
* Run `git clone https://github.com/BlockResearchGroup/WS_cluster.git`

> **Example**
>
> On Windows
> ```bash
> mkdir %USERPROFILE%\Code
> mkdir %USERPROFILE%\Code\Workshops
> cd %USERPROFILE%\Code\Workshops
> git clone https://github.com/BlockResearchGroup/WS_cluster.git
> ```
>
> On Mac
> ```bash
> mkdir -p ~/Code/Workshops
> cd ~/Code/Workshops
> git clone https://github.com/BlockResearchGroup/WS_cluster.git
> ```

**2. Create an environment and install COMPAS.**

Change into the repository folder you just cloned and run

```bash
cd WS_cluster
conda env create -f environment.yml
conda activate workshop
```

**3. Check the installation**

Launch the Python interpreter and import `compas`, `compas_rhino`, `compas_ghpython`.

On Windows: type `python` in Anaconda Prompt
<br />On Mac: type `python` in Terminal

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
run the following from Anaconda Prompt (on Windows) or Terminal (on Mac):

```bash
python -m compas_rhino.install -v 5.0 -p compas compas_rhino compas_ghpython
```

> **Note** (Windows only)
>
> Use `-v 6.0` instead of `-v 5.0` if you want to use Rhino 6 instead of Rhino 5.

Open Rhino and run the script [verify_rhino.py](verify_rhino.py).
If this does not throw an error and prints the correct COMPAS version (`0.4.20`),
Rhino is properly configured.

> **Note**
>
> To run a script in Rhino, just type `RunPythonScript` at the Rhino command prompt
> and select the script you want to run.

**5. Set up your development environment**

You can use any development environment that you're comfortable with,
but the instructions for this workshop are written for [VS Code](https://code.visualstudio.com/).

We recommend installing the following extensions

* Python
* EditorConfig

Open the *Extensions* view by clicking on the icon on the left of VS Code, search for the extensions using the search box, and install them. Then open the workspace of the workshop (`WS_cluster/workshop.code-workspace`) using `File > Open Workspace...`.

Finally, run `verify_editor.py` to check the setup. If this prints `0.4.20`, VS Code is properly configured.

> **Note**
>
> To simply run the script, right-click and select `Run Python File in Terminal...`.
> 
> To use the debugger, open the *Debug* view by clicking the icon on the left of VS Code and select the configuration for your OS. Then just hit `F5`.


## Examples

*   Network
    *   shortest path (plot): [network_shortestpath.py](examples/network_shortestpath.py)
        <br />*Plot the shortest path between two vertices of a network.*
    *   shortest path (interactive plot): [network_shortestpath.py](examples/network_shortestpath.py)
        <br />*Plot the shortest path between a given start vertex and a point picked by the user.*
    *   equilibrium (dynamic plot): [network_equilibrium.py](examples/network_equilibrium.py)
        <br />*Plot the dynamic relaxation process of a network with randomly prescribed edge force densities.*
*   Mesh
    *   subdivision (Rhino): [mesh_subdivision_rhino.py](examples/mesh_subdividion_rhino.py)
        <br />*Generate a subdivision surface using a control mesh.*
    *   smoothing on surface (Rhino): [mesh_smoothing_rhino.py](examples/mesh_smoothing_rhino.py)
        <br />*Smooth a mesh on a given target surface.*
*   RPC
    *   ...

## Troubleshooting

*No problems so far...*
