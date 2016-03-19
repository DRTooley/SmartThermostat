#!/usr/bin/env python3

import os
import time
import sys

import TempuratureHardwareManager as THM
import ThermostatGUI as TG

def CleanThermostat():
    Cleaner = THM.TempuratureHardwareManager()
    Cleaner.hardware.DoCleanUp()



if __name__ == "__main__":
    ## This is needed incase of fatal error
    ## There will be threads going in the background
    ## and the GPIO will be on and must be cleaned
    if len(sys.argv) > 1:
        if '-clean' in sys.argv:
            CleanThermostat()

    else:
        app = TG.ThermostatApp(None)
        app.title("Smart Thermostat Alpha")
        app.mainloop()
