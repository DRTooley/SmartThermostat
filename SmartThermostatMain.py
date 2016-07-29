#!/usr/bin/env python3

import sys

from DebuggingControl import Debug
from HardwareManager import HardwareManager
from ThermostatGUI import ThermostatApp

def CleanThermostat():
    Cleaner = HardwareManager()
    Cleaner.DoCleanUp()



if __name__ == "__main__":
    ## The -clean command is needed in case of an error
    ## There will be threads going in the background
    ## and the GPIO will be on and must be cleaned
    
    debugSet = {'-d','-D','-debug'}
    if set.intersection(debugSet, set(sys.argv)):
        Debug(True)
    if Debug().GetInfo() is None:
        Debug(False)
    if '-clean' in sys.argv:
        CleanThermostat()
    else:
        app = ThermostatApp(None)
        app.title("Smart Thermostat Alpha")
        app.mainloop()
