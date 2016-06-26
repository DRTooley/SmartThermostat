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

    debugSet = {'-d','-D','-debug'}
    if debugSet.intersect(set(sys.argv)):
        d = Debug(True)
    if '-clean' in sys.argv:
        CleanThermostat()
    else:
        app = TG.ThermostatApp(None)
        app.title("Smart Thermostat Alpha")
        app.mainloop()
