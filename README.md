## Vixon


Vixon (short for VisCon or Visual Controller) as the name suggests is an automation application to control usual tasks like Typing using a keyboard, Reading / Media / Presentation using Visual actions.

I started working on this over a weekend with the aim of learning about popular algorithms being used in Gesture Detection, Tracking movement of objects, Color detection etc.


### Demo

For the restless, Just click on the thumbnail to watch it in action :wink:

[![Vixon](https://i.ytimg.com/vi/FO7A14QEAOM/hqdefault.jpg)](http://bit.do/prnvdixit_vixon)

If the above link is not working for some reason, [Click here](https://youtu.be/FO7A14QEAOM)


### Advantages

* Just click on whatever object you want to track - corresponding HSV colour space range would be calculated automatically to aid gesture detection. This defers from other approaches I came across of as you have to manually set the HSV ranges using Hit-&-Trial in them. Saves a lot of time with a quite a decent accuracy! :smile:

* A preventive measure in case the program begins working unexpectedly is to move the mouse cursor to extreme left (that was already a part of PyAutoGUI framework - I added it for detection program as well)

* To stop detection, you can just press 's' after keeping openCV window in focus. If you wish to automate the same, just set the detection-inhibitor HSV range (by right clicking on the object you want to use as a detection-inhibitor) {In the demo, the orange colour acts as such a preventive measure}, and whenever that object is in front of camera, no gesture detection of any object would be done. :smiley:


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


### Contributor
* **Pranav Dixit** - [*GitHub*](https://github.com/prnvdixit) - [*LinkedIn*](https://www.linkedin.com/in/prnvdixit/)


### Reviews / Feature Requests
I would love to hear from you, contact me via [Telegram](https://telegram.me/prnvdixit) or shoot me a [mail](mailto:prnvdixit@gmail.com).
