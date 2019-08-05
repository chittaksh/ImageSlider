from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
import media_sources

class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='right')

        # get all the images for the slide show.
        mediaList = media_sources.getMedia()

        for src in mediaList:
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel


CarouselApp().run()