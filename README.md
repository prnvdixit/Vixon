## Vixon


Vixon (short for VisCon or Visual Controller) as the name suggests is an automation application to control usual tasks like Typing using a keyboard, Reading / Media / Presentation using Visual actions.

I developed this project with the aim of learning about popular algorithms being used in Image processing for Gesture Detection, Tracking movement of objects, Color detection etc.


### Demo

For the restless, Just click on the thumbnail to watch it in action :wink:

[![Vixon](https://i.ytimg.com/vi/FO7A14QEAOM/hqdefault.jpg)](http://bit.do/prnvdixit_vixon)

If the above link is not working for some reason, [Click here](https://youtu.be/FO7A14QEAOM)


### Advantages

* Just click on whatever object you want to track - corresponding HSV colour space range would be calculated automatically to aid gesture detection. This defers from other approaches I came across of as you have to manually set the HSV ranges using Hit-&-Trial in them. Saves a lot of time with a quite a decent accuracy! :smile:

* A preventive measure in case the program begins working unexpectedly is to move the mouse cursor to extreme left (that was already a part of PyAutoGUI framework - I added it for detection program as well)

* To stop detection, you can just press 's' after keeping openCV window in focus. If you wish to automate the same, just set the detection-inhibitor HSV range (by right clicking on the object you want to use as a detection-inhibitor) {In the demo, the orange colour acts as such a preventive measure}, and whenever that object is in front of camera, no gesture detection of any object would be done. :smiley:


### Working

For the sake of others, I am sharing a brief gist of the working of the application. :smile:

Still, if anything is not clear enough in code or you want to be explained here, just [contact me](https://github.com/prnvdixit/Vixon/blob/master/README.md#reviews--feature-requests).

I used PyGame for video streaming and other stuff, mostly because of the mouse-control actions and rendering options it provide (plus, I already had previous experience working with it :stuck_out_tongue:). Every left click selects particular portion of the frame and calculates the corresponding HSV colour range for that portion. Similarly, every right click does so for detection-inhibitor object.

For tracking the object, I used OpenCV's ```cv2.inRange``` function. Before that, for cleaning up and reducing the noise in a frame - I used Blurring functions and Morphological transformations. Next, contours were detected and maximum contour out of all was selected as "most probable object".  On each frame, the mid point of the biggest contour was stored to create a trail of motion.
For detecting direction of movement, I maintained a vector and once it's magnitude exceeds a particular threshold value, direction corresponding to starting point was calculated.

### Installation requirements

* [Python 2.7.*](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [Numpy](www.numpy.org/)
* [PyGame](https://pypi.python.org/pypi/Pygame)
* [imutils](https://pypi.python.org/pypi/imutils)
* [PyAutoGUI](https://pypi.python.org/pypi/PyAutoGUI)


### Note

Some approaches I used earlier but ultimately didn't included them :-
* I had earlier kept automatic mode selection (keyboard, media, reading, presentation) using {number of} fingers, but I was facing problems in my laptop's lower quality webcam (worked well enough when using my Smartphone's 13MP camera though :stuck_out_tongue:), so I had to switch to manual way of doing so.

* I haven't used the area based approach for keyboard typing (the key is assumed to be clicked when your finger is at definite distance from screen) as that restricts you from sitting relaxably and typing. :sweat:


### Developer
* **Pranav Dixit** - [*GitHub*](https://github.com/prnvdixit) - [*LinkedIn*](https://www.linkedin.com/in/prnvdixit/)


### Reviews / Feature Requests
I would love to hear from you, contact me via [Telegram](https://telegram.me/prnvdixit) or shoot me a [mail](mailto:prnvdixit@gmail.com).

