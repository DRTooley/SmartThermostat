#!/usr/bin/env python3

import os
import time
import sys
import tkinter

import HardwareManager as HM
import ThermostatGUI as TG

def CleanThermostat():
    Cleaner = HM.HardwareManager()
    Cleaner.DoCleanUp()



if __name__ == "__main__":
    ## This is needed incase of fatal error
    ## There will be threads going in the background
    ## and the GPIO will be on and must be cleaned
    if len(sys.argv) > 1:
        if '-clean' in sys.argv:
            CleanThermostat()

    else:
        app = TG.ThermostatApp()
        app.title("Smart Thermostat Alpha")
        app.mainloop()
