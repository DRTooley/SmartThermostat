import threading

import TempuratureHardwareManager as THM
import TempuratureMeter as TM
import TempuratureReader as TR

class ThermometerState():
    Undefined, Comfortable, Heating, Cooling = range(4)

class TempuratureControlLogic():
    def __init__(self, ThreadTimes, Cold = 70, Hot = 74):
        self.state = ThermometerState.Undefined
        self.tempurature = None
        self.threadValidator = ThreadTimes

        self.hardware = THM.TempuratureHardwareManager()
        self.tempuratureControl = TM.TempuratureMeter(Cold, Hot)
        self.tempuratureKeeper = TR.TempuratureReader(self.threadValidator)
        self.MainLogicThread()

    def MainLogicThread(self):
        CurrentTemp_Avg = self.tempuratureKeeper.average_tempurature()
        if CurrentTemp_Avg != None:
            print("The average tempurature is: %.2f" % CurrentTemp_Avg)
            self.DetermineState(CurrentTemp_Avg)
        if self.threadValidator.isRunning():
            waitTime = self.threadValidator.GetMainLogicThreadWaitTime()
            threading.Timer(waitTime, self.MainLogicThread).start()

    def DetermineState(self, Temp):
        self.setTempurature(Temp)

        if self.state == ThermometerState.Comfortable:
            self.ComfortLogic()
        elif self.state == ThermometerState.Heating:
            self.HeatingLogic()
        elif self.state == ThermometerState.Cooling:
            self.CoolingLogic()
        else:
            self.DefaultLogic()

    def ComfortLogic(self):
        self.DefaultLogic()
        self.hardware.Off()
        print("Comfort")
        

    def HeatingLogic(self):
        self.DefaultLogic(1)
        self.hardware.StartHeat()
        print("Heating")

    def CoolingLogic(self):
        self.DefaultLogic(-1)
        self.hardware.StartCool()
        print("Cooling")

    def DefaultLogic(self, differential=0):
        if self.tempurature <= self.tempuratureControl.getCoolLimit() + differential:
            self.state = ThermometerState.Heating
        elif self.tempurature >= self.tempuratureControl.getHeatLimit() + differential:
            self.state = ThermometerState.Cooling
        else:
            self.state = ThermometerState.Comfortable


    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def setTempurature(self, tmp):
        self.tempurature = tmp
 
    def getTempurature(self):
        return self.tempurature

