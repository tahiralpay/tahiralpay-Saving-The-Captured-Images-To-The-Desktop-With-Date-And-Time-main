"""
                       EKİM 2020 TALPAY                  
"""

from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor
from datetime import datetime
import time

camera = PiCamera()
pir = MotionSensor(4)
i = 0
k = 0

filename = "Date:{0:%d}-{0:%m}-{0:%y} Time:{0:%H}-{0:%M}-{0:%S}".format(datetime.now())

def foto():
    camera.start_preview()
    sleep(1)
    camera.capture('/home/pi/Desktop/%s.jpg' % filename)
    camera.stop_preview()

def video():
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/%s.h264' % filename)
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()
       
while True:
    if pir.wait_for_no_motion:
        print("hareket_yok=", k)
        k += 1
        time.sleep(1)
        
        if k>60:
            k = 0
            i = 0
            
    if pir.motion_detected:
        print("hareket_var=", i)
        i += 1
        time.sleep(1)
            
        if i == 1:
            foto()
        
        if i == 7:
            video()
            i = 0
            k = 0
    
    

                
    
           
    
    

    
    
