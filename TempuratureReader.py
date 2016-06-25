
import glob
import threading

import TempuratureSensor as TS
from SmartThermostatMain import Debugging

class TempuratureReader():
    def __init__(self, ThreadTimes):

        self.current_tempurature_sensors = {}
        self.threadValidator = ThreadTimes
        self.validSensorCount = None
        self.sensorDirectoryLocation = '/sys/bus/w1/devices/28-*'
        if Dubugging:
            self.sensorDirectoryLocatoion = "DebugTempuratureSensors/*"
            
        self.PopulateCurrentTempuratureFiles()
            
    def StartPopulateCurrentTempuratureFiles(self):
        if self.threadValidator.isRunning():
            waitTime = self.threadValidator.GetPopulateSensorFilesWaitTime()
            t = threading.Timer(waitTime, self.PopulateCurrentTempuratureFiles).start()
            self.threadValidator.SetPopulateSensorFilesTimerThread(t)

    def PopulateCurrentTempuratureFiles(self):
        self.RemoveLostFiles()
        file_list = self.FindTempuratureFiles()
        for file in file_list:
            try:
                self.current_tempurature_sensors[file]
            except KeyError:
                self.current_tempurature_sensors[file] = TS.TempuratureSensor(file, self.threadValidator)

        self.StartPopulateCurrentTempuratureFiles()
        
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
    
