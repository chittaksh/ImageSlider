import os, sys
import config
import Sources.local_storage as local

def getMedia():
    # Return image list. 
    imageList = []
    
    # If the application is running in demo mode
    if config.EnableDemo:
        # Location for demo directory
        demoDirectory = os.path.expanduser(config.DemoDirectory)

        # Get list of demo images.
        demoImages = local.getImageList(demoDirectory)
        imageList.extend(demoImages)

    # If the application
    if config.EnableLocal:
        # Location for local picture directory
        localDirectory = os.path.expanduser(config.LocalDirectory)

        # Get images from local picture directory.
        localImages = local.getImageList(localDirectory)
        imageList.extend(localImages)
    
    #if config.EnableDrive:
            
    return imageList
