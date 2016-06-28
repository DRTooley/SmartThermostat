
import glob
import time
import threading

import TempuratureSensor as TS
from DebuggingControl import Debug

class TempuratureReader():
    def __init__(self, ThreadTimes):

        self.current_tempurature_sensors = {}
        self.threadValidator = ThreadTimes
        self.validSensorCount = None
        self.sensorDirectoryLocation = '/sys/bus/w1/devices/28-*'
        debug = Debug()
        if debug.GetInfo():
            print("Using dummy sensor files!")
            self.sensorDirectoryLocation = "DebugTempuratureSensor/*"
            
        self.PopulateCurrentTempuratureFiles()
            
    def StartPopulateCurrentTempuratureFiles(self):
        t = threading.Thread(target=self.PopulateCurrentTempuratureFiles)
        t.daemon = True
        t.start()
        self.threadValidator.SetPopulateSensorFilesTimerThread(t)

    def PopulateCurrentTempuratureFiles(self):
        waitTime = self.threadValidator.GetPopulateSensorFilesWaitTime()
        while True:
            time.sleep(waitTime)
            self.RemoveLostFiles()
            file_list = self.FindTempuratureFiles()
            for filename in file_list:
                try:
                    self.current_tempurature_sensors[filename]
                except KeyError:
                    self.current_tempurature_sensors[filename] = TS.TempuratureSensor(filename, self.threadValidator)

        
    def RemoveLostFiles(self):
        for key, TempSensor in self.current_tempurature_sensors.items():
            if not TempSensor.isRunning():
                del self.current_tempurature_sensors[key]

    def FindTempuratureFiles(self):
        dir_list = glob.glob(self.sensorDirectoryLocation)
        file_list = [file+'/w1_slave' for file in dir_list]
        return file_list


    def AverageTempurature(self):
        tempurature_list = []
        for key, TempSensor in self.current_tempurature_sensors.items():
            if TempSensor.getTempuratureValid():
                tempurature_list.append(TempSensor.getTempurature()) 
        if len(tempurature_list) > 0: 
            self.validSensorCount = len(tempurature_list)
            return sum(tempurature_list)/len(tempurature_list)
        else:
            self.validSensorCount = 0
            return None

    def GetValidSensorCount(self):
        return self.validSensorCount

    def FindLowestTempurature(self):
        lowest = -1000
        for key, tempSensor in self.current_tempurature_sensors.items():
            if tempSensor.getTempuratureValid():
                if lowest == -1000:
                    lowest = tempSensor.getTempurature()
                else:
                    if lowest > tempSensor.getTempurature():
                        lowest = tempSensor.getTempurature()     

        return lowest

    def FindHighestTempurature(self):
        highest = -1001
        for key, tempSensor in self.current_tempurature_sensors.items():
            if tempSensor.getTempuratureValid():
                if highest == -1001:
                    highest = tempSensor.getTempurature()
                else:
                    if highest < tempSensor.getTempurature():
                        highest = tempSensor.getTempurature()     

        return highest
    
