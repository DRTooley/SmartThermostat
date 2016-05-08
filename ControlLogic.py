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
        self.tempurature = -1002
        self.threadValidator = ThreadTimes
        self.tempuratureControl = TempMeter

        self.hardware = HM.HardwareManager()
        self.tempuratureKeeper = TR.TempuratureReader(self.threadValidator)
        self.StartControlLogicThread()

    def StartControlLogicThread(self):
        if self.threadValidator.isRunning():
            waitTime = self.threadValidator.GetControlLogicWaitTime()
            t = threading.Timer(waitTime, self.ControlLogicThread).start()  
            self.threadValidator.SetControlLogicTimerThread(t)

    def ControlLogicThread(self):
        CurrentTemp_Avg = self.tempuratureKeeper.AverageTempurature()
        
        self.DetermineState(CurrentTemp_Avg)
        
        self.StartControlLogicThread()

    def DetermineState(self, Temp):
        if Temp is None:
            self.SetTempurature(-1002)
            self.hardware.Off()
            self.SetState(ThermometerState.Undefined)
        
        else:    
            self.SetTempurature(Temp)

            if self.GetState() == ThermometerState.Comfortable:
                self.ComfortLogic()
            elif self.state == ThermometerState.Heating:
                self.HeatingLogic()
            elif self.GetState() == ThermometerState.Cooling:
                self.CoolingLogic()
            elif self.GetState() == ThermometerState.Fan:
                self.hardware.StartFan()
            elif self.GetState() == ThermometerState.Off:
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
            self.SetState(ThermometerState.Heating)
        elif self.tempurature >= self.tempuratureControl.GetHeatLimit() + differential:
            self.SetState(ThermometerState.Cooling)
        else:
            self.SetState(ThermometerState.Comfortable)


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

    def CleanUpHW(self):
        self.TurnOff()
        self.hardware.DoCleanUp()

