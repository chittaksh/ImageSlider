from Screens.start_screen import ImageSlider

# Find a way to get access to HDMI on raspberry pi and start slide show remotely.
#import os
#os.environ["KIVY_BCM_DISPMANX_ID"] = "2"

if __name__ == '__main__':
    print('This is the init for the main.')
    ImageSlider().run()
