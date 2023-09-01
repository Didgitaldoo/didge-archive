# check if all data exists for each didge and if the filenames are correct
# python -m scripts.check_filenames

import json
from typing import Dict, List
import os

types = {
    "name": str,
    "stl-files": list,
    "blender-files": list,
    "audio-samples": dict,
    "geometry": str
}

for didge in json.load(open("didge-archive.json", "r")):
    
    for attr in ("name", "stl-files", "blender-files", "audio-samples", "geometry"):
        if not attr in didge:
            print(f"Missing attribute '{attr}' in didge {didge['name']}")

        if type(didge[attr]) != types[attr]:
            print(f"Attribute '{attr}' of didge '{didge['name']}' should be {types[attr]}, is {type(didge[attr])}")

        for attr in ("hand-closed", "neutral-sound", "short-song"):
            if not attr in didge["audio-samples"]:
                print(f"Missing attribute '{attr}' in didge {didge['name']}/audio-samples")
            
            file = didge["audio-samples"][attr]
            if not os.path.exists(file):
                print(f"File '{file}' in didge '{didge['name']}' does not exist.")

    if not os.path.exists(didge["geometry"]):
        print(f"File '{didge['geometry']}' in didge '{didge['name']}' does not exist.")

    if len(didge["blender-files"]) == 0:
        print(f"Didge '{didge['name']}' has no blender files")

    for file in didge["blender-files"]:
        if not os.path.exists(file):
            print(f"File '{file}' in didge '{didge['name']}' does not exist.")

    for file in didge["stl-files"]:
        if not os.path.exists(file):
            print(f"File '{file}' in didge '{didge['name']}' does not exist.")

    if len(didge["stl-files"]) == 0:
        print(f"Didge '{didge['name']}' has no stl files")