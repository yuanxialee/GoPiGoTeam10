Lab3 Submission
Group Spyndra 
Team Members: Yuanxia Lee (yl3262) and Yan-Song Chen (yc3240)

Main program: navigate.py
It imports standard packages as well as map.py, convex_hull.py, graph.py, and rover.py.
Rover.py imports util.py which imports control.py
Link: https://www.youtube.com/watch?v=-XlLeyQF8ng
There are 3 combined videos in the link. It was unclear which of the 3 actually resulted in the closest distance to the goal. The videos start at 0:00, 0:28, and 0:56 (which is also mentioned in the video description on youtube)

The simulation part works as described. Navigate.py takes in 2 arguments, the first being the text file used and the second argument being the number of centimeters that we want to grow the obstacles by. We used a square growth (taking the square that would be circumscribed around the circle created by the robot's diameter) which is why the growth argument only needs one number, and we typically used 24 (though we did mess around with 26). We have a variety of classes and methods that allow us to read in the file, create obstacles, grow them out, convex hull them, create the visibility graph, and use dijkstra's algorithm. We plot all of these and display it in our code in navigate.py in lines 85 (obstacle points, grown obstacle points with convex hull), 118 (grown obstacles filled in as polygons), 134 (visibility graph), and 137 (dijkstra's path in red). We included these plots in this zipped folder; the plots took in arguments of roborace.txt and 24. We often comment out these points when running the robot in order to not have to exit so many plots before allowing the robot to move. Conversely, when not running the code on the robot, we comment out lines 12, 33, and 141-157 (the end) as our computers do not have the gopigo software that rover.py imports. 
