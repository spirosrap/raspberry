# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
DS = 7
ST_CP = 11
SH_CP = 13

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(DS, GPIO.OUT) ## Setup DS
GPIO.setup(ST_CP, GPIO.OUT) ## Setup ST_CP
GPIO.setup(SH_CP,GPIO.OUT)## Setup SH_CP

GPIO.output(SH_CP,False)
GPIO.output(DS,False)
GPIO.output(ST_CP,False)

state=[0,0,0,0,0,0,0,0]
def setbit(n,value):
   global state
   state[n]=value
   for i in state:
       GPIO.output(DS,i==1)
       GPIO.output(SH_CP,True)
       GPIO.output(DS,i==1)
       GPIO.output(SH_CP,False)
   GPIO.output(ST_CP,True)
   GPIO.output(ST_CP,False)

def setbyte(l):
   for i in l:
       GPIO.output(DS,i==1)
       GPIO.output(SH_CP,True)
       GPIO.output(DS,i==1)
       GPIO.output(SH_CP,False)
   GPIO.output(ST_CP,True)
   GPIO.output(ST_CP,False)

for i in range(0,8):
   GPIO.output(DS,False)
   GPIO.output(SH_CP,True)
   GPIO.output(DS,False)
   GPIO.output(SH_CP,False)

for i in range(0,8):
   GPIO.output(DS,True)
   GPIO.output(SH_CP,True)
   GPIO.output(DS,True)
   GPIO.output(SH_CP,False)


GPIO.output(ST_CP,True)
GPIO.output(ST_CP,False)

#setbit(3,1)
for i in range(0,8):
    setbit(i,1)
    time.sleep(0.4)
    setbit(i,0)

setbyte([1,1,0,0,1,1,1,1])
