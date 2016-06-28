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
    ## The -clean command is needed in case of an error
    ## There will be threads going in the background
    ## and the GPIO will be on and must be cleaned

    debugSet = {'-d','-D','-debug'}
    if set.intersection(debugSet, set(sys.argv)):
        d = Debug(True)
    if Debug().GetInfo() is None:
        Debug(False)
    if '-clean' in sys.argv:
        CleanThermostat()
    else:
        app = TG.ThermostatApp(None)
        app.title("Smart Thermostat Alpha")
        app.mainloop()
