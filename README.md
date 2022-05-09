# Saving-The-Captured-Images-To-The-Desktop-With-Date-And-Time

Circuit Diagram
<p align="center">
  <img width="450" height="562" src="https://user-images.githubusercontent.com/75435070/165791673-4de0b31c-38e3-4107-a7d0-78076a6db77a.png">
</p>

After detecting the first motion, two different counters, motion_on and motion_off, run. motion_on counter starts counting as soon as PIR sensor is active and stops counting when motion stops. The movement_off counter starts counting as soon as the movement stops. If motion is detected During the counting of motion_off counter, motion_on counter becomes active again. "one" second after motion is detected, the photo mode is activated and the image is taken. at this stage, if motion is not detected for “1” minute, the motion_on counter is reset and the program returns to the beginning. “6” seconds after the motion is detected, the video mode is activated and a “10”-second image is taken, the motion_on and motion_off counters are reset and the captured images are saved on the desktop

![Ekran Alıntısı](https://user-images.githubusercontent.com/75435070/165792299-76fd5917-6293-4008-bd80-c17ea56faec6.PNG)
![dvdsv](https://user-images.githubusercontent.com/75435070/165792307-78ae4354-6e3e-4db1-9b93-1a212a7ace19.PNG)
