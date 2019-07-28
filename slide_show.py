'''
Python 3 slideshow using tkinter and pillow (PIL)
Used to show images one after the other. reads config from settings.py
'''

import tkinter as tk
from PIL import Image, ImageTk
import time
import media_sources
import config

class Start(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.window = MySlideShow(self)
        self.window.startSlideShow()

class MySlideShow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        #remove window decorations 
        self.overrideredirect(True)
        #set the background to black
        self.configure(background='black')

        #save reference to photo so that garbage collection
        #does not clear image variable in show_image()
        self.persistent_image = None
        self.pixNum = 0

        #used to display as background image
        self.label = tk.Label(self)
        self.label.pack(side="top", fill="both", expand=True)

        self.mediaList = media_sources.getMedia()
    
    def startSlideShow(self, delay=config.DelayTime): #delay in seconds
        # Change this block of code to return something.
        if(len(self.mediaList) <= 0):
            self.displayMessage('Something went wrong while loading images.')
            raise Exception('Something went wrong while loading images.')

        # Read the image from the array.
        myimage = self.mediaList[self.pixNum]
        self.pixNum = (self.pixNum + 1) % len(self.mediaList)
        self.showImage(myimage)
        #its like a callback function after n seconds (cycle through pics)
        self.after(delay*1000, self.startSlideShow)

    def showImage(self, filename):
        image = Image.open(filename)  
        
        # reads the size of the image and screen, and resizes the image for the screen.
        img_w, img_h = image.size
        scr_w, scr_h = self.winfo_screenwidth(), self.winfo_screenheight()
        if img_w > scr_w or img_h > scr_h:
            ratio = min(scr_w/img_w, scr_h/img_h)
            img_w = int(img_w*ratio)
            img_h = int(img_h*ratio)
            image = image.resize((img_w,img_h), Image.ANTIALIAS)

        # takes the full screen to show the image.
        self.wm_geometry("{}x{}+{}+{}".format(scr_w,scr_h,0,0))
        
        # create new image 
        self.persistent_image = ImageTk.PhotoImage(image)
        self.label.configure(image=self.persistent_image)
        # assign black background to the label.
        self.label.configure(background='black')

    def displayMessage(self, message):
        # add code to display text message
        print(message)
