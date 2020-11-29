# Copyright (c) 2019 - 2020 Elie Michel
#
# This file is part of LilySurfaceScraper, a Blender add-on to import
# materials from a single URL. It is released under the terms of the GPLv3
# license. See the LICENSE.md file for the full text.

bl_info = {
    "name": "Lily Surface Scraper",
    "author": "Élie Michel <elie.michel@exppad.com>",
    "version": (1, 5, 2),
    "blender": (2, 82, 0),
    "location": "Properties > Material",
    "description": "Import material from a single URL",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/eliemichel/LilySurfaceScraper/issues",
    "support": "COMMUNITY",
    "category": "Import",
}

import sys
import os

script_file_directory = os.path.dirname(os.path.realpath(__file__))
site_packages_path = os.path.join(script_file_directory, "site-packages")

if not os.path.exists(site_packages_path):
    os.makedirs(site_packages_path)

sys.path.append(site_packages_path)

try:
    from lxml import etree
except:
    import subprocess
    python_binary =  sys.executable
    try:
        subprocess.run([python_binary, '-m', 'ensurepip'], check=True)
        subprocess.run([python_binary, '-m', 'pip', 'install', 'lxml', '-t', site_packages_path], check=True)
    except subprocess.SubprocessError as error:
        print(error.output)

def isImportedInBlender():
    try:
        import bpy
        return True
    except ImportError:
        return False


if isImportedInBlender():
    from . import preferences
    from . import frontend
    from .callback import register_callback

    def register():
        preferences.register()
        frontend.register()
        
    def unregister():
        frontend.unregister()
        preferences.unregister()

    if __name__ == "__main__":
        register()

else:
    from .WorldData import WorldData
    from .MaterialData import MaterialData
    from .ScrapersManager import ScrapersManager
