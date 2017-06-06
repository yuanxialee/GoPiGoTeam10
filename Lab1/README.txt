Lab1
Yuanxia Lee and Yan-Song Chen
yl3262, yc3240

Part1: basicmv.py
works as described

Part2: dance.py
works as described

Part3: sensora.py
test1 results
90
87
85
82
80
77
76
73
71
68
66
62
60

actual end distance was 21 cm instead of 30 cm


test2 results:
100
78
76
110
96
99
102
101
99
96
92
90
87
85
82
79
75
73
70
67
65
61

noisy and non-linear return distances 
actual end result was 55 cm instead of 60 cm


test3 results*:
starting from test3 we set the speed to 100, whereas the previous tests had no such setting
39
39
36
35
33
32
31

ended at 23 cm instead of 30 cm


test4 results:
22
22
24
26
28
30
33
32
30

overshot its perceived 30cm and returned 
ended at 22 cm instead of 30cm


test5 results:
45
43
43
40
39
37
35
34
31
31

curved to the left slightly
ended at 21 cm instead of 30 cm


Part4: sensorf.py
For this program, we placed the robot 25.5 centimeters away from th object and set the left edge (left if you're facing the object) of the object right in the middle of the robot's two "eyes." Then, we have the robot turn to the left (in the space where the object is not extending into) some theta that is returned and stops once it reads an anomalously large result. From the theta that is returned and our known original distance from the object, we can calculate the width of the beam. We set the theta to start at 79 degrees because that was the number that actually gave us 90 degrees in the physical world. We tested the program we wrote 5 times at 25 cm distance, with results being 33.7 cm, 31.2 cm, 31.2 cm, 28.8 cm, and 33.7 cm. Not counting peak values and then taking the average, we determined the sensor width to be 32.0 cm. We also tested 5 times at 35 centimeteres (changing the distance variable in the code accordingly) and received the results of 31.2 cm, 31.2 cm, 31.2, cam, 31.2 cm, and 34. 1 cm. These are very close to our original result of 32.0 cm for the width of the cone. The angle returned was smaller, but this makes sense as the greater the distance the lesser the angle. 

Part5:
