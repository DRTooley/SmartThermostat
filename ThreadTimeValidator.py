import time

class ThreadOptions():
    def __init__(self, wait_time, thread_timer = None):
        self.waitTime = wait_time
        self.threadTimer = thread_timer


class ThreadTimeValidator():
    __instance = None
    def __new__(cls):
        if ThreadTimeValidator.__instance is None:
            ThreadTimeValidator.__instance = object.__new__(cls)
            # Wait time in seconds for each function to be rerun
            cls.controlLogicTO = ThreadOptions(0.5)
            cls.sensorUpdateTO = ThreadOptions(1.0)
            cls.populateSensorFilesTO = ThreadOptions(2.5)
            cls.updateDisplayTO = ThreadOptions(0.1)

            cls.running = True

        return ThreadTimeValidator.__instance

    def GetUpdateDisplayWaitTime(cls):
        return cls.updateDisplayTO.waitTime

    def SetUpdateDisplayWaitTime(cls, time):
        cls.updateDisplayTO.waitTime = time

    def GetControlLogicWaitTime(cls):
        return cls.controlLogicTO.waitTime

    def SetControlLogicWaitTime(cls, time):
        cls.controlLogicTO.waitTime = time

    def GetSensorUpdateWaitTime(cls):
        return cls.sensorUpdateTO.waitTime

    def SetSensorUpdateWaitTime(cls, time):
        cls.sensorUpdateTO.waitTime = time

    def GetPopulateSensorFilesWaitTime(cls):
        return cls.populateSensorFilesTO.waitTime

    def SetPopulateSensorFilesWaitTime(cls, time):
        cls.populateSensorFilesTO.waitTime = time

    def SetUpdateDisplayTimerThread(cls, thread):
        cls.updateDisplayTO.threadTimer = thread

    def SetControlLogicTimerThread(cls, thread):
        cls.controlLogicTO.threadTimer= thread

    def SetSensorUpdateTimerThread(cls, thread):
        cls.sensorUpdateTO.threadTimer = thread

    def SetPopulateSensorFilesTimerThread(cls, thread):
        cls.populateSensorFilesTO.threadTimer = thread

    def isRunning(cls):
        return cls.running

    def Exit(self):
        self.running = False


        
