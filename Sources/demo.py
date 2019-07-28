import os
import sys
import config

def getImages():
    imageList = []
    demo_dir = config.DemoDirectory

    # Check if the directory exists.
    if not (os.path.lexists(demo_dir)):
        os.mkdir(demo_dir)

    # Start scanning the directory for all the png and jpg files.
    for root, dirs, files in os.walk(demo_dir):
        for f in files:
            if f.endswith(".png") or f.endswith(".jpg"):
                img_path = os.path.join(root, f)
                # print(img_path)
                imageList.append(img_path)

    return imageList