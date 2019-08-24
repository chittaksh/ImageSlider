from Screens.start_screen import ImageSlider
import os
os.environ["KIVY_BCM_DISPMANX_ID"] = "2"

if __name__ == '__main__':
    print('This is the init for the main.')
    ImageSlider().run()
