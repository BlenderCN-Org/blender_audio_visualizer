#----------------------------------------------------------
# File __init__.py
#----------------------------------------------------------

#    Addon info
bl_info = {
    "name": "Audio Visualizer",
    "author": "David Schommer",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "View3D",
    "description": "Visualize audio",
    "warning": "",
    "wiki_url": "",
    "category": "Audio",
    }


# Source: http://wiki.blender.org/index.php/Dev:Py/Scripts/Cookbook/Code_snippets/Multi-File_packages
# To support reload properly, try to access a package var,
# if it's there, reload everything
if "bpy" in locals():
    import imp
    # reload other python files
    imp.reload(speaker.py)
    imp.reload(controller.py)
    print("Reloaded multifiles")
else:
    from . import mycube, mysphere, mycylinder
    print("Imported multifiles")

import bpy

# UI code goes here
