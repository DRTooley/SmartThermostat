#!/usr/bin/env python3

import os
import time
import sys
import tkinter

from DebuggingControl import Debug
import HardwareManager as HM
import ThermostatGUI as TG

def CleanThermostat():
    Cleaner = HM.HardwareManager()
    Cleaner.DoCleanUp()



if __name__ == "__main__":
    Debug(False)
    
    ## This is needed incase of fatal error
    ## There will be threads going in the background
    ## and the GPIO will be on and must be cleaned

    if len(sys.argv) > 1:
        debugSet = {'-d','-D','-debug'}
        if '-clean' in sys.argv:
            CleanThermostat()
        elif '-d' in debugSet:
            d = Debug(True)
            if d:
                print(d)
    
            

    else:
        app = TG.ThermostatApp(None)
        app.title("Smart Thermostat Alpha")
        app.mainloop()
