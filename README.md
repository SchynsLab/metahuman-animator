# metahuman-animator
Proof of concept for Python-based MetaHuman animation for psychophysics research.
Check the [wiki](https://github.com/SchynsLab/metahuman-animator/wiki) for more information.

## Scripts

As stated in the wiki, we recommend executing Python code in Unreal via the [VSCode extension](https://marketplace.visualstudio.com/items?itemName=NilsSoderman.ue-python). The `master.py` script in this repository is a first attempt
at writing a script that fully automates adding a MetaHuman to an Unreal world and
animating it via its facial/body rig. It was created mainly via trial-and-error and there's
no clear plan on how to package this in an interface (CLI, Python package/module, or otherwise).

## Assets

The `assets/` directory contains some Unreal assets like a default world (`default_world.uasset`)
and an example sequence (`default_sequence.uasset`). The `mp4_render_config.uasset` is a custom
asset to easily render sequences as mp4 files. (Haven't found out how to incorporate this
into the script.)
