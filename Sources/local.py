import os
import sys
import config

def getImages():
    imageList = []
    curr_dir = os.path.expanduser(config.LocalDirectory)

    # Check if the directory exists.
    if not (os.path.lexists(curr_dir)):
        os.mkdir(curr_dir)

    # Start scanning the directory for all the png and jpg files.
    for root, dirs, files in os.walk(curr_dir):
        for f in files:
            if f.endswith(".png") or f.endswith(".jpg"):
                img_path = os.path.join(root, f)
                # print(img_path)
                imageList.append(img_path)

    return imageList