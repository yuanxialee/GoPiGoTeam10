Lab4 Submission
Group Spyndra 
Team Members: Yuanxia Lee (yl3262) and Yan-Song Chen (yc3240)

Main program: track.py
It imports standard packages as well as dip.py and rover.py.
rover.py imports util.py which imports control.py
hsv_color.py is a standalone program to pick an hsv color
pick_obj.py is a standalone program used to draw a rectangle around the desired target area that gets cropped (shows you what you cropped) and returns the reference points of the rectangle. 

Link: Run 1: https://www.youtube.com/watch?v=msGDMIX29Io	Run 2: https://www.youtube.com/watch?v=Bbqb_1cQTbE
We have 2 videos to demonstrate our program. 

Track.py works best using a neon green object with no other objects of similar color nearby. We chose a ball as our object as it will always appear as a circle in our camera (vs choosing a rectangular object). In the program, we continuously take pictures until the object has been tracked or is deemed untrackable (untrackable objects are objects lifted too high for the camera as the camera has no vertical changing abilities and cannot maintain a fixed distance as it cannot know if the object is too close or a small object that is too far away). However, for the first picture, we don't use since upon starting, the first camera picture is always darker. Then, we average the next 3 binarized picture areas in order to determine the fixed distance we want the robot to work towards. In the while loop, we have the robot take the picture, threshold it, and find the center and area. If the center is to the left of the vertical center axis, we have gopigo turn left, and the same for the right. If the area is larger than the original area we gave it, it backs up, and moves forward if smaller. We do allow a tolerance of 15 for the axis and have a function to calculate the tolerance we allow for the area (for the tolerance is less when it's farther away and greater when it's closer due to more pixel variation). After the object has been tracked, we also have the captured images, their binary form, and the picture with the centroid as a red dot (which we've combined into our videos). 