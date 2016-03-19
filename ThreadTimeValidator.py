

class ThreadTimeValidator():
    def __init__(self):
        # Wait time in seconds for each function to be rerun
        self.mainLogicThreadWaitTime = 2.0
        self.sensorUpdateWaitTime = 3.0
        self.populateSensorFilesWaitTime = 15.0
        self.running = True

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
