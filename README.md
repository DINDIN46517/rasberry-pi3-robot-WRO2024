About teams:
We are the TurboBot team from Prince Royal's College. We have Din Kumpun and JingJing on the team. We are like the steering wheel that controls the team's car or robot on the track. To drive according to the goal and handle obstacles smoothly We organize and divide work duties carefully. Even though this is our first WRO future engineer competition, But we are very committed to our work. We put everything we know into our work. To make the work come out the best

Roles:
We divide our duties into three main categories:
1. Program: In this role, Din and Kumpum have the main responsibilities. They have the greatest coding aptitude in the team. Therefore, this role is suitable for them.
2. Hardware (circuit connection): In this duty, everyone has a role in connecting Din and Kumpun circuits to the robot. JingJing is responsible for connecting the circuits in the program to include in the document and as a manual for connecting the circuits.
3. Document-JingJing is the main editor. The team's work is compiled into documents. 3D modeling And the work is followed, and photos are taken to see the progress of the robot. Making flowcharts and various diagrams
In our work, we use the principles of the engineering design process to solve various problems.

Robot Design:
Basic structure: Our robot uses a Raspberry Pi 5 board for control. It is controlled by the Python language. The front wheels of the robot have a steering function, that is, changing the direction of the car by rotating to adjust the direction of the front wheels to match the desired direction, and the rear wheels of the robot have a steering function. Differential: adjusting the rotation of the wheels on both sides of the car differently to help the car turn smoothly. And our car has a wheel base reduction feature, designing the car structure to have the least distance between the two wheels. To increase the turning angle

Movement: Built-in, our robot uses There are two motors for driving: Servo Motor 88004 on the front wheels of the car. by rotating by degrees To be used to turn the car at various angles and M Motor 8883 in the rear wheels of the car. Used for running straight and back. Both motors are cheap. Slow-fast control through the robot shield that has a motor driver system using LEGO motors. It makes it convenient to connect to the car frame built from LEGO.
Color detector: Our team uses Raspberry Pi Cam Module 3 to detect color bars because the camera has a wide field of view. I can read colors accurately. The camera will read the color as HSV values. We read the RGB color value from the ground to know when our robot have to turn using Rev color sensor

Sensors: Our team uses three ultrasonic sensors around the vehicle: front, left, and right. It works based on the reflection of frequency waves with objects by connecting it to the Raspberry Pi. We added a Battery to supply power to the Ultrasonic. We use Gyro to control the direction of turning more precisely. It can also calculate the robot's revolutions., which will be the main sensor in the work.

Power supply: Our team initially used a power bank as a power source with a Raspberry Pi 3, but when we switched to using a Raspberry Pi 5 with a Servo Motor 88004 and an M Motor 8883, we discovered that the power bank did not supply enough power. Which make the robot stop working halfway. So we switched to a 9V battery and converted the power to 5V through the Robot Shield before powering the Raspberry Pi.

Problem solving:
First round of racing: when pressing the yellow button The robot ran straight for a while. When the front sensor reads the distance to the wall, The left and right sensors read which side has the greatest distance and then turn approximately 90 degrees to that side. Along with recording which side you turned and how many turns you had made. The gyro sensor keeps the robot running on the middle preventing hitting the edge. When it completes 3 turns or 12 turns, it will come back to rest in the position it was released from.

Second round: Press the green button. The robot ran out of the frame and ran straight. Then the camera will detect the color value. If the color bar is red, the car should turn right. If the color bar is green, the car should turn left. The reading of the distance will be according to the boundaries that we created to find near-farness.And the Rev color sensor reads the color of the floor. If it reads blue, have the robot turn 90 degrees left and if it reads orange, have the robot turn 90 degrees right. Then let the camera detect the color stick, and so on. When three rounds are complete, stop in the starting position.

Summary:
The robot is controlled from the Raspberry Pi 5 board, detects color bars from the Raspberry Pi Cam module 3, uses the Rev color sensor to read the color on the floor, reads the distance between the wall and the robot with ultrasonic sensors, and uses Gyro for control. To make the better movement, we use the robot shield to convert the power and control the motor. We use the Servo Motor 88004 to rotate by degrees and the M Motor 8883 for running straight and back. We use a 9-volt battery to supply power.

What we learned:
We learned to work as a team. Solving immediate problems and finding solutions.Making common and AI program, designing robots with principles, creating documents, studying and analyzing problems, and much more.

Special thanks:
We would like to thank our team and mentors, who constantly support our work and have had good experiences from this competition. Gathering the judges who answered our questions. Thank you.
