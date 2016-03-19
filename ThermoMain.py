#!/usr/bin/env python3


##################################################################
### Needed Features
###
### 1) User Tempurature Input Acceptance
### This should be in the form of control over the tempurature range
### that is acceptable. The high/low values can change independantly
### but must be at least two degrees different
###   - This may require that I change the heat/cool logic of going
###     one degree more/less than desired temp.
###
### 2) User Information Output
### Once mounted how will this convey information to the user?
### Req:
###   - Current Temp (AVG)
###   - Min/Max Temp (DEBUG)
###   - Current State (Heat/Cool/Fan Only)
###
### 3) Fan Only Mode User Input
### On occation Fan Only Mode is requested; I must accept this input
### During Fan Only Mode Tempurature will be ignored and the Fan will 
### always remain ON
###
### 4) Thermostat OFF
### In this state tempurature will be ignored and there will be no 
### heating or cooling
###
### 5) SMART Mode
### Recognise our phones connecting to WiFi and change tempurature 
### preferences accordingly
###
### 6) LEARNING Mode
### Research machine learning algorithms to determine what might be
### benificial. This would include a database setup to record past
### data and analysis
###
### 7) History Database
### This will enable the learning feature to truly view past data 
### and make informed future decisions
###
###
###
###

##################################################################
### Know Issues
###
### 1)
### If Hot is lost on tempurature sensors but the information wire
### is not the tempurature file will report 0 degrees Celcius for
### that sensor while still reporting valid data. This will lead to 
### errant calculations.
###
### 2) Fixed?
### If a sensor Information wire is lost for a long period of time
### the information file will disapper. This leads to an IOError
### being thrown by the SensorReader thread. This will cause the 
### tempuratures to stop updating. Handle a file disappearing and
### kill the associated class
###
### To Correct this I created a variable to keep track of which 
### sensor files are still running; I had them stop queuing themself
### if they found an IOError and they will be removed from the dictionary
### of TempuratureReader. If the file returns it will be repopulated into
### the list and a new instance will be made
###
### 3) Fixed?
### Check the return value of average tempurature to ensure validity
### When this is not done; in the event that no sensors are reporting 
### It will cause the program to crash.
###
### I did a simple check to see if the result was None; if so do nothing
### and requeue yourself
###
###
###

import os
import time
import sys

import TempuratureControlLogic as TCL
import TempuratureReader as TR
import TempuratureHardwareManager as THM

if __name__ == "__main__":

    Cleaner = THM.TempuratureHardwareManager()
    
    if len(sys.argv) > 1:
        if '-clean' in sys.argv:
            Cleaner.hardware.DoCleanUp()

    else:
        TempuratureKeeper = TR.TempuratureReader()
        TempController = TCL.TempuratureControlLogic()

        while(True):
            CurrentTemp_Avg = TempuratureKeeper.average_tempurature()

            if CurrentTemp_Avg != None:
                print("The average tempurature is: %.2f" % CurrentTemp_Avg)
                TempController.DetermineState(CurrentTemp_Avg)

            time.sleep(4)
    
    #os.system('modprobe w1-gpio')
    #os.system('modprobe w1-therm')
    #temp_sensor_1 = '/sys/bus/w1/devices/28-000007670b20/w1_slave'
    #temp_sensor_2 = '/sys/bus/w1/devices/28-00000765fa34/w1_slave'

