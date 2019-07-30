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

        # go full screen
        self.attributes("-fullscreen", True)

        # set the background color to black.
        self.config(background=config.SliderBackgroundColor)

        # remove window decorations 
        self.overrideredirect(True)

        # create a slideShow window. 
        self.window = MySlideShow(self)
        self.window.startSlideShow()

class MySlideShow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self)
        
        # Save reference to photo so that garbage collection
        # does not clear image variable in show_image()
        self.persistent_image = None
        self.pixNum = 0

        self.config(background=config.SliderBackgroundColor)

        # get all the images for the slide show.
        self.mediaList = media_sources.getMedia()

        # This decides where to place the controls.
        # This allowed the code to work on windows as well.
        self.place(x=0,y=0)

        # create label to set the image as background
        self.label = tk.Label(self)
        self.label.pack(side="top", fill="both", expand=1)

        # Add controls here in future to add images. 
    
    def startSlideShow(self, delay=config.DelayTime): #delay in seconds
        # change this block of code to return something.
        if(len(self.mediaList) <= 0):
            self.displayMessage('Something went wrong while loading images.')
            raise Exception('Something went wrong while loading images.')
        
        # Read the image from the array.
        myimage = self.mediaList[self.pixNum]
        self.pixNum = (self.pixNum + 1) % len(self.mediaList)
        self.showImage(myimage)
        # its like a callback function after n seconds (cycle through pics)
        self.after(delay*1000, self.startSlideShow)

    def showImage(self, filename):
        pilImage = Image.open(filename)

        # get the screen size.
        scr_w, scr_h = self.winfo_screenwidth(), self.winfo_screenheight()

        # set the screen size to full screen.
        self.label.config(width=scr_w, height=scr_h)

        # reads the size of the image.
        img_w, img_h = pilImage.size
        
        # resize the image size to fit the screen.
        if img_w > scr_w or img_h > scr_h:
            ratio = min(scr_w/img_w, scr_h/img_h)
            img_w = int(img_w*ratio)
            img_h = int(img_h*ratio)
            pilImage = pilImage.resize((img_w, img_h), Image.ANTIALIAS)

        self.label.config(background=config.SliderBackgroundColor)

        # create new image 
        self.persistent_image = ImageTk.PhotoImage(pilImage)
        self.label.configure(image=self.persistent_image)

    def displayMessage(self, message):
        # add code to display text message
        self.label.config(text=message)
        print(message)
