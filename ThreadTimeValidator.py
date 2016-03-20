

class ThreadTimeValidator():
    def __init__(self):
        # Wait time in seconds for each function to be rerun
        self.mainLogicThreadWaitTime = 2.0
        self.sensorUpdateWaitTime = 3.0
        self.populateSensorFilesWaitTime = 8.0
        self.updateDisplayWaitTime = 1.0
        self.running = True

    def GetUpdateDisplayWaitTime(self):
        return self.updateDisplayWaitTime

    def GetMainLogicThreadWaitTime(self):
        return self.mainLogicThreadWaitTime

    def GetSensorUpdateWaitTime(self):
        return self.sensorUpdateWaitTime

    def GetPopulateSensorFilesWaitTime(self):
        return self.populateSensorFilesWaitTime

    def isRunning(self):
        return self.running

    def Exit(self):
        self.running = False
