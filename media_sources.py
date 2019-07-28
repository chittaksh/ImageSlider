import config
import Sources.local as local

def getMedia():
    # Return image list. 
    imageList = []
    
    # If the application is running in 
    if config.EnableLocal:
        demoImages = local.getImages()
        imageList.extend(demoImages)
    
    #if config.EnableDrive:
            
    return imageList
