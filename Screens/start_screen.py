# base Class of your App inherits from the App class. 
from kivy.app import App 
from kivy.core.window import Window
from Screens.slider.slide_show import CarouselApp

# the Base Class of our Kivy App 
class ImageSlider(App):  
    def build(self): 
        Window.fullscreen = True
        # return the proper view.
        return CarouselApp()