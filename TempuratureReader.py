
import glob
import threading
import TempuratureSensor as TS

class TempuratureReader():
    def __init__(self, ThreadTimes):
        self.current_tempurature_sensors = {}
        self.threadValidator = ThreadTimes
        self.validSensorCount = None
        self.PopulateCurrentTempuratureFiles()
        

    def PopulateCurrentTempuratureFiles(self):
        self.RemoveLostFiles()
        file_list = self.FindTempuratureFiles()
        for file in file_list:
            try:
                self.current_tempurature_sensors[file]
            except KeyError:
                self.current_tempurature_sensors[file] = TS.TempuratureSensor(file, self.threadValidator)

        if self.threadValidator.isRunning():
            waitTime = self.threadValidator.GetPopulateSensorFilesWaitTime()
            threading.Timer(waitTime, self.PopulateCurrentTempuratureFiles).start()
        
    def RemoveLostFiles(self):
        for key, TempSensor in self.current_tempurature_sensors.items():
            if not TempSensor.isRunning():
                del self.current_tempurature_sensors[key]

    def FindTempuratureFiles(self):
        dir_list = glob.glob('/sys/bus/w1/devices/28-*')
        file_list = [file+'/w1_slave' for file in dir_list]
        return file_list


    def average_tempurature(self):
        tempurature_list = []
        for key, TempSensor in self.current_tempurature_sensors.items():
            if TempSensor.getTempuratureValid():
                tempurature_list.append(TempSensor.getTempurature()) 
        if len(tempurature_list) > 0: 
            self.validSensorCount = len(tempurature_list)
            return sum(tempurature_list)/len(tempurature_list)
        else:
            return None

    def GetValidSensorCount(self):
        return self.validSensorCount

    def FindLowestTempurature(self):
        lowest = None
        for key, tempSensor in self.current_tempurature_sensors.items():
            if tempSensor.getTempuratureValid():
                if lowest is None:
                    lowest = tempSensor.getTempurature()
                else:
                    if lowest > tempSensor.getTempurature():
                        lowest = tempSensor.getTempurature()     

        return lowest

    def FindHighestTempurature(self):
        highest = None
        for key, tempSensor in self.current_tempurature_sensors.items():
            if tempSensor.getTempuratureValid():
                if highest is None:
                    highest = tempSensor.getTempurature()
                else:
                    if highest < tempSensor.getTempurature():
                        highest = tempSensor.getTempurature()     

        return highest
    
