import threading

import HardwareManager as HM
import TempuratureReader as TR

class ThermometerState():
    numberOfThermometerStates = 6
    Undefined, Comfortable, Heating, Cooling, Fan, Off = range(numberOfThermometerStates)

    def GetStateText(state):
        if state == 1:
            return "Comfort"
        elif state == 2:
            return "Heating"
        elif state == 3:
            return "Cooling"
        elif state == 4:
            return "Fan Only"
        elif state == 5:
            return "Off"
        else:
            return "Undefined"


class ControlLogic():
    def __init__(self, ThreadTimes, TempMeter):
        self.state = ThermometerState.Undefined
        self.tempurature = None
        self.threadValidator = ThreadTimes
        self.tempuratureControl = TempMeter

        self.hardware = HM.HardwareManager()
        self.tempuratureKeeper = TR.TempuratureReader(self.threadValidator)
        self.MainLogicThread()

    def MainLogicThread(self):
        CurrentTemp_Avg = self.tempuratureKeeper.average_tempurature()
        if CurrentTemp_Avg != None:
            self.DetermineState(CurrentTemp_Avg)
        if self.threadValidator.isRunning():
            waitTime = self.threadValidator.GetMainLogicThreadWaitTime()
            threading.Timer(waitTime, self.MainLogicThread).start()

    def DetermineState(self, Temp):
        self.SetTempurature(Temp)

        if self.state == ThermometerState.Comfortable:
            self.ComfortLogic()
        elif self.state == ThermometerState.Heating:
            self.HeatingLogic()
        elif self.state == ThermometerState.Cooling:
            self.CoolingLogic()
        elif self.state == ThermometerState.Fan:
            self.hardware.StartFan()
        elif self.state == ThermometerState.Off:
            self.hardware.Off()
        else:
            self.DefaultLogic()

    def ComfortLogic(self):
        self.DefaultLogic()
        self.hardware.Off()

    def HeatingLogic(self):
        self.DefaultLogic(1)
        self.hardware.StartHeat()

    def CoolingLogic(self):
        self.DefaultLogic(-1)
        self.hardware.StartCool()

    def DefaultLogic(self, differential=0):
        if self.tempurature <= self.tempuratureControl.GetCoolLimit() + differential:
            self.state = ThermometerState.Heating
        elif self.tempurature >= self.tempuratureControl.GetHeatLimit() + differential:
            self.state = ThermometerState.Cooling
        else:
            self.state = ThermometerState.Comfortable


    def SetState(self, state):
        if state >= 0 and state < ThermometerState.numberOfThermometerStates:
            self.state = state

    def GetState(self):
        return self.state

    def GetAverageTempurature(self):
        return self.tempurature

    def SetTempurature(self, temp):
        self.tempurature = temp

    def GetLowestTempurature(self):
        return self.tempuratureKeeper.FindLowestTempurature()

    def GetHighestTempurature(self):
        return self.tempuratureKeeper.FindHighestTempurature()

    def FanOn(self):
        self.SetState(ThermometerState.Fan)

    def TurnOff(self):
        self.SetState(ThermometerState.Off)

    def TurnOn(self):
        self.SetState(ThermometerState.Undefined)

    def GetValidSensorCount(self):
        return self.tempuratureKeeper.GetValidSensorCount()

