import config
import Sources.local as local
import Sources.demo as demo

def getMedia():
    # Return image list. 
    imageList = []
    
    # If the application is running in demo mode
    if config.EnableDemo:
        demoImages = demo.getImages()
        imageList.extend(demoImages)

    # If the application is running in 
    if config.EnableLocal:
        localImages = local.getImages()
        imageList.extend(localImages)
    
    #if config.EnableDrive:
            
    return imageList
