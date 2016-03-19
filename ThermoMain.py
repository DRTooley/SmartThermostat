#!/usr/bin/env python3

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

