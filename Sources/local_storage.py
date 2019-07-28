import os
import sys

def getImageList(location):
    imageList = []

    # Check if the directory exists.
    if not (os.path.lexists(location)):
        os.mkdir(location)

    # Start scanning the directory for all the png and jpg files.
    for root, dirs, files in os.walk(location):
        for f in files:
            if f.endswith(".png") or f.endswith(".jpg"):
                img_path = os.path.join(root, f)
                # print(img_path)
                imageList.append(img_path)

    return imageList