#todo: speed, code should only have if(lane) once in loop

from picamera.array import PiRGBArray
from picamera import PiCamera

import cv2
import numpy as np
from settings import *

import time

from collections import deque

import threading
import logging

##timeEntry = False
##t0 = time.time()
#initialize time, just to get into main's scope

import RPi.GPIO as GPIO

import sys

import pygame


##lower_time_factor = 0.85#this may not be doing anything,
#move to constructor?
##first_lowered = False

##screen_length = 0.97

delay_time_down = .04
delay_time_release = .01

LedPin = 11    # pin11
LedPin2 = 12

LedPin3 = 15
LedPin4 = 13

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led

    GPIO.setup(LedPin2, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin2, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led

    GPIO.setup(LedPin3, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin3, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led

    GPIO.setup(LedPin4, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.output(LedPin4, GPIO.LOW) # Set LedPin high(+3.3V) to turn on led

def worker(num,Lane):
##    print num

##    if num 

    
##    time.sleep(2.75*num*lower_time_factor)
    time.sleep(2.75*num)

##    time.sleep(.26)

    if Lane == 1:
##        cv2.circle(frame,(L1,H2), 10, RED, -1)
##        print "tap lane 1"
        GPIO.output(LedPin, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(delay_time_release)

    elif Lane == 2:
##        cv2.circle(frame,(L2,H2), 10, RED, -1)
##        print "tap lane 2"
        GPIO.output(LedPin2, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin2, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
    elif Lane == 3:
##        cv2.circle(frame,(L3,H2), 10, RED, -1)
##        print "tap lane 3"
        GPIO.output(LedPin3, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin3, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
        
    elif Lane == 4:
##        cv2.circle(frame,(L4,H2), 10, RED, -1)
##        print "tap lane 4"
        GPIO.output(LedPin4, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin4, GPIO.LOW)  # led on
        time.sleep(delay_time_release)

def worker_simple(num,Lane):
    time.sleep(num)#do not multiply by lower time factor

##    time.sleep(.26)

    if Lane == 1:
##        cv2.circle(frame,(L1,H2), 10, RED, -1)
        print "tap lane 1"
        GPIO.output(LedPin, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(delay_time_release)

    elif Lane == 2:
##        cv2.circle(frame,(L2,H2), 10, RED, -1)
        print "tap lane 2"
        GPIO.output(LedPin2, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin2, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
    elif Lane == 3:
##        cv2.circle(frame,(L3,H2), 10, RED, -1)
        print "tap lane 3"
        GPIO.output(LedPin3, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin3, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
        
    elif Lane == 4:
##        cv2.circle(frame,(L4,H2), 10, RED, -1)
        print "tap lane 4"
        GPIO.output(LedPin4, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin4, GPIO.LOW)  # led on
        time.sleep(delay_time_release)


def doubleTapWorker(num,Lane,c):
##    time.sleep(2.5* num * lower_time_factor)
    time.sleep(2.75* num)

##    print Lane

##    time.sleep(.26)
##    print Lane

    if Lane == 1:
##        print "tap tap lane 1"
        GPIO.output(LedPin, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
        c.set_val(0)

    elif Lane == 2:
####        cv2.circle(frame,(L2,H2), 10, RED, -1)
##        print "tap tap lane 2"
        GPIO.output(LedPin2, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin2, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
        c.set_val(0)
    elif Lane == 3:
##        cv2.circle(frame,(L3,H2), 10, RED, -1)
##        print "tap tap lane 3"
        GPIO.output(LedPin3, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin3, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
        c.set_val(0)
        
    elif Lane == 4:
##        cv2.circle(frame,(L4,H2), 10, RED, -1)
##        print "tap tap lane 4"
        GPIO.output(LedPin4, GPIO.HIGH)  # led on
        time.sleep(delay_time_down)

        GPIO.output(LedPin4, GPIO.LOW)  # led on
        time.sleep(delay_time_release)
        c.set_val(0)

##def keyboardListener(number):
##    pygame.init()
##
##    print "hello"
##    while True:
##        events = pygame.event.get()
##        for event in events:
##            if(event.type == KEYUP) or (event.type == KEYDOWN):
##                print "key pressed"

    
class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start #no doubles at start
    def set_val(self,val):
##        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
##            logging.debug('Acquired lock')
            self.value = val
##            logging.debug('Waiting for worker threads')
##            print self.value
        finally:
            self.lock.release()
            
    def get_val(self):
        self.lock.acquire()
        try:
            return self.value
        finally:
            self.lock.release()
        
class TimeMarker():
    def __init__(self):
        self.last_time = time.time()
        self.t1 = time.time()

        self.LastLane = 0

##        self.circular_queue = \
##        deque(np.repeat(AVG_INIT,AVG_SIZE),maxlen=AVG_SIZE)
        self.circular_queue = deque([0.3,0.3,0.3,0.3,0.3,0.3,0.3], maxlen=AVG_SIZE)

        self.currentAVG = 0.3

##        self.first_lowered = False
##        self.second_lowered = False
        
        # need to put a "fake" .01 case at the end to prevent index out of bounds
        self.tier_arr = np.array([.17,.13,.11,.08,.05,.02,.02,.02,0])
##        self.tier_arr = np.array([.19,0,0,0,0])
##        self.Lower_arr = np.array([0.80,.70,.65,.60,.55,.50,.45,.40,.35])
        self.Lower_arr = np.array([0.80,.75,.70,.65,.60,.55,.50,.45,.40])

##        self.trigger = np.array([False,False])
        self.tier_i = 0
        
        self.my_lower_time = 0.85

##        self.doubleTap = np.zeros((5,), dtype=int)

##    def get_currentAVG():
##        return self.currentAVG
##    def set_doubleTap(self,lane,number):
##        self.doubleTap[lane] = number


    def movingAverage(self,values):
        weights = np.repeat(1.0,AVG_SIZE)/AVG_SIZE
        smas = np.convolve(values,weights,'valid')
        return smas[0]
        
    def markTime(self,BlackLane):
    ##    if timeEntryBool == True:
        if(BlackLane != self.LastLane):
            self.t1 = time.time()
            #1.329 inches on calipers

            currentMeasure = (self.t1 - self.last_time)

##            print currentMeasure

##            if currentMeasure >= .31:
##                currentMeasure = .31

               
            #lower time factor, only do this once.
##            if cv2.waitKey(25) & 0xFF == ord('a'):
##                print "lowering time factor to ",self.tier_i
##                self.my_lower_time = self.Lower_arr[self.tier_i]
##                self.tier_i += 1
##            elif (self.currentAVG <= .16) and (self.second_lowered == False):
##                print "lowering time factor to 0.65"
##                self.my_lower_time = .70
##                self.second_lowered = True

            t = threading.Thread\
                (target = worker, args=(self.currentAVG*self.my_lower_time,BlackLane,))
            threads.append(t)
            t.start()

            if abs((self.circular_queue[-1] - currentMeasure)) < .08 and currentMeasure < self.circular_queue[-1]:
##            self.circular_queue.append( 1.0 / (self.t1 - self.last_time) )
                print currentMeasure
                self.circular_queue.append( currentMeasure )
                self.currentAVG = self.movingAverage(self.circular_queue)
            
            self.LastLane = BlackLane
            self.last_time = time.time()

            return True
        else:
            return False

##        else: # there is a possibility of double/triple block
            
    def checkHeight(self,H):
        if frame[H, L1, 0] > 150:
            pass
##            cv2.circle(frame,(L1,H), 5, AQUA, -1)
        else:
            return 1
##            self.markTime(1)
##            cv2.circle(frame,(L1,H), 5, RED, -1)
          
        if frame[H, L2, 0] > 150:
            pass
##            cv2.circle(frame,(L2,H), 5, AQUA, -1)
        else:
            return 2
##            self.markTime(2)
##            cv2.circle(frame,(L2,H), 5, RED, -1)
##            return 2
          
        if frame[H, L3, 0] > 150:
            pass
##            cv2.circle(frame,(L3,H), 5, AQUA, -1)
        else:
            return 3
##            self.markTime(3)
##            cv2.circle(frame,(L3,H), 5, RED, -1)
##            return 3
          
        if frame[H, L4, 0] > 150:
            pass
##            cv2.circle(frame,(L4,H), 5, AQUA, -1)
        else:
##            self.markTime(4)
##            cv2.circle(frame,(L4,H), 5, RED, -1)
            return 4

##        return 0 # no black lane found!

    def try_tap(self,lane,counterObj):
##        print counterObj.get_val(), lane
##        print lane
##        if(lane == 1):
##            counterObj.set_val(1)
##            a = threading.Thread\
##            (target = doubleTapWorker, args=(self.currentAVG,lane,counterObj,))
##            a.start()
##            return
##            print " lane is 1"
        
        if( counterObj.value == 0):# if not already currently double tapping lane #
##            print lane

##            self.doubleTap[lane] = 1 #might need thread locking
            counterObj.set_val(1)
            a = threading.Thread\
            (target = doubleTapWorker, args=(self.currentAVG*self.my_lower_time,lane,counterObj,))
##            threads.append(a)
            a.start() # note this can still cause more than one threads named "a"
        else:
            pass

    def simple_tap(self,BlackLane,number): 
        t = threading.Thread\
                (target = worker_simple, args=(number,BlackLane,))
        threads.append(t)
        t.start()

        

setup() # setup GPIO's

PianoCalibration = np.load('PianoCalibration.npz')

HighMid = PianoCalibration['HighMid']
H3 = PianoCalibration['H3']
H2 = PianoCalibration['H2']
H1 = PianoCalibration['H1']
L1 = PianoCalibration['L1']
L2 = PianoCalibration['L2']
L3 = PianoCalibration['L3']
L4 = PianoCalibration['L4']

threads = []

##k = threading.Thread\
##            (target = keyboardListener, args=(1,))
####            threads.append(a)
##k.start() # note this can still cause more than one threads named "a"

##t1 = threading.Thread(target = worker, args=(self.currentAVG,black_lane_hm,))
##                threads.append(t)

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
##cap = cv2.VideoCapture('my_video.h264')

timer = TimeMarker()

counter1 = Counter()
##counter1.set_val(1)
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()

triplecounter1 = Counter()
triplecounter2 = Counter()
triplecounter3 = Counter()
triplecounter4 = Counter()




 
# Check if camera opened successfully
##if (cap.isOpened()== False):
##    print("Error opening video stream or file")

dead_frame = np.zeros([0],dtype=np.uint8)

###################### camera setup
camera = PiCamera()
camera.resolution = (WIDTH, HEIGHT)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(WIDTH, HEIGHT))

# allow the camera to warmup
time.sleep(0.1)
#####################

for img in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    frame = img.array

    black_lane_h2 = timer.checkHeight(H2) #int (1,2,3 or 4) storing black lane number
    black_lane_h3 = timer.checkHeight(H3)
##    black_lane_hm = timer.checkHeight(HighMid)

##    timer.try_tap(black_lane_hm,counter1)
##    timer.try_tap(black_lane_h2,counter2)
    
    if(black_lane_h2 == 1): timer.simple_tap(black_lane_h2,0)
    elif(black_lane_h2 == 2): timer.simple_tap(black_lane_h2,0)
    elif(black_lane_h2 == 3): timer.simple_tap(black_lane_h2,0)
    elif(black_lane_h2 == 4): timer.simple_tap(black_lane_h2,0)

    if(black_lane_h3 == 1): timer.simple_tap(black_lane_h3,.33) #tried .303, then bumped up to .33
    elif(black_lane_h3 == 2): timer.simple_tap(black_lane_h3,.33)
    elif(black_lane_h3 == 3): timer.simple_tap(black_lane_h3,.33)
    elif(black_lane_h3 == 4): timer.simple_tap(black_lane_h3,.33)


    if cv2.waitKey(25) & 0xFF == ord('a'):
        print "lowering time factor to ",timer.tier_i
        timer.my_lower_time = timer.Lower_arr[timer.tier_i]
        timer.tier_i += 1

    

##    cv2.line(frame,(0,H1),(240,H1),VIOLET,1)
            

##    cv2.imshow('Frame',frame)

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    break #only do this loop once

##time.sleep(5)
##sys.exit() #for now add a "breakpoint" here
    

  
for img in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
##    print "currentAVG is :",timer.currentAVG
    frame = img.array

    

    black_lane_hm = timer.checkHeight(HighMid) #int (1,2,3 or 4) storing black lane number

    if( timer.markTime( black_lane_hm ) == False ):
    #double or triple possibility, check h3 AND HighMid

        # move H3 down 10 pixels and check it
        black_lane_h3 = timer.checkHeight(H3 + 6)
                
        if( black_lane_h3 == black_lane_hm ):
##            print "at least double detected"
##            print "double in lane ",black_lane_h3
            if(black_lane_h3 == 1): timer.try_tap(black_lane_hm,counter1)
            elif(black_lane_h3 == 2): timer.try_tap(black_lane_hm,counter2)
            elif(black_lane_h3 == 3): timer.try_tap(black_lane_hm,counter3)
            elif(black_lane_h3 == 4): timer.try_tap(black_lane_hm,counter4)

            black_lane_h2 = timer.checkHeight(H2 + 6)

            if( (black_lane_h2 == black_lane_hm) and (black_lane_h2 == black_lane_h3) ):
##                print "triple in lane ",black_lane_h2
                if(black_lane_h2 == 1): timer.try_tap(black_lane_hm,triplecounter1)
                elif(black_lane_h2 == 2): timer.try_tap(black_lane_hm,triplecounter2)
                elif(black_lane_h2 == 3): timer.try_tap(black_lane_hm,triplecounter3)
                elif(black_lane_h2 == 4): timer.try_tap(black_lane_hm,triplecounter4)##
    ##            if (black_lane_h2 == black_lane_hm):
    ##                print "triple detected in lane ",black_lane_h2

            
                    
    ##        timer.markTime( timer.checkHeight(HighMid) )
            # and don't pass in timer anymore
            
##    cv2.line(frame,(0,H1),(240,H1),VIOLET,1)
            

    cv2.imshow('dead_frame',frame)

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    if cv2.waitKey(25) & 0xFF == ord('a'):
        print "lowering time factor to ",timer.tier_i
        timer.my_lower_time = timer.Lower_arr[timer.tier_i]
        timer.tier_i += 1

            # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break



 

GPIO.output(LedPin, GPIO.LOW)   # led off
GPIO.output(LedPin2, GPIO.LOW)   # led off
GPIO.output(LedPin3, GPIO.LOW)   # led off
GPIO.output(LedPin4, GPIO.LOW)   # led off
GPIO.cleanup()                  # Release resource
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
