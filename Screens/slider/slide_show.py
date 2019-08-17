# base Class of your App inherits from the App class. 
from kivy.app import App 
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
import Sources.media_sources as mediaSources
from kivy.core.window import Window

class CarouselApp(Carousel):
    def __init__(self, **var_args):
        super(CarouselApp, self).__init__(**var_args)

        # get all the images for the slide show.
        mediaList = mediaSources.getMedia()

        for src in mediaList:
            image = AsyncImage(source=src, allow_stretch=True)
            self.add_widget(image)