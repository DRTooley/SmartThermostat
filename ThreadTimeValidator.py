import time

class ThreadOptions():
    def __init__(self, wait_time, thread_timer = None):
        self.waitTime = wait_time
        self.threadTimer = thread_timer


class ThreadTimeValidator():
    def __init__(self):
        # Wait time in seconds for each function to be rerun
        self.controlLogicTO = ThreadOptions(1.0)
        self.sensorUpdateTO = ThreadOptions(1.0)
        self.populateSensorFilesTO = ThreadOptions(2.5)
        self.updateDisplayTO = ThreadOptions(0.1)

        self.allThreadOptions = [
            self.controlLogicTO,
            self.sensorUpdateTO,
            self.populateSensorFilesTO,
            self.updateDisplayTO
            ]

        self.running = True

    def GetUpdateDisplayWaitTime(self):
        return self.updateDisplayTO.waitTime

    def SetUpdateDisplayWaitTime(self, time):
        self.updateDisplayTO.waitTime = time

    def GetControlLogicWaitTime(self):
        return self.controlLogicTO.waitTime

    def SetControlLogicWaitTime(self, time):
        self.controlLogicTO.waitTime = time

    def GetSensorUpdateWaitTime(self):
        return self.sensorUpdateTO.waitTime

    def SetSensorUpdateWaitTime(self, time):
        self.sensorUpdateTO.waitTime = time

    def GetPopulateSensorFilesWaitTime(self):
        return self.populateSensorFilesTO.waitTime

    def SetPopulateSensorFilesWaitTime(self, time):
        self.populateSensorFilesTO.waitTime = time

    def SetUpdateDisplayTimerThread(self, thread):
        self.updateDisplayTO.threadTimer = thread

    def SetControlLogicTimerThread(self, thread):
        self.controlLogicTO.threadTimer= thread

    def SetSensorUpdateTimerThread(self, thread):
        self.sensorUpdateTO.threadTimer = thread

    def SetPopulateSensorFilesTimerThread(self, thread):
        self.populateSensorFilesTO.threadTimer = thread

    def isRunning(self):
        return self.running

    def Exit(self):
        self.running = False
        for TO in self.allThreadOptions:
            if TO.threadTimer is not None:
                TO.threadTimer.cancel()

        for TO in self.allThreadOptions:
            if TO.threadTimer is not None:
                TO.threadTimer.join()

        # Allow other processes to exit
        time.sleep(1.0)
        
