# ImageSlider
Project to automate the image sliding(from different sources) on raspberry pi

### Requirements:
Python3\
pipreqs (pip install pipreqs)


### Run:
Install the required packages. (pip install -r requirements.txt)\
Add images to the Demo folder to be displayed (for test purpose).\
Python3 main.py

### Adding Images:
#### Unix system:
Add images to the Pictures folder on unix file system. Then run the application.

#### Windows system:
Add images to the Pictures folder. Then run the application.

### Updates:
Currently just works with .png and .jpg on local storage.

### Future:
Add support for google drive, dropbox and one drive for image sources.\
Add image caching.\
Add customisations for timer.\
Add support for video.

### FAQ
#### I get an error regarding ktinker on unix based system.
Ans: sudo apt-get install python3-tk

#### How to set up kivy for raspberry
sudo apt-get autoremove --purge

sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip xsel libjpeg-dev

pip3 install Cython pillow

pip3 install kivy
