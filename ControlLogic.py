import threading

import HardwareManager as HM
import TempuratureReader as TR

numberOfThermometerStates = 6
class ThermometerState():
    Undefined, Comfortable, Heating, Cooling, Fan, Off = range(numberOfThermometerStates)

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
            print("The average tempurature is: %.2f" % CurrentTemp_Avg)
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
            print("Fanning")
        elif self.state == ThermometerState.Off:
            self.hardware.Off()
            print("System Off")
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
        if self.tempurature <= self.tempuratureControl.GetCoolLimit() + differential:
            self.state = ThermometerState.Heating
        elif self.tempurature >= self.tempuratureControl.GetHeatLimit() + differential:
            self.state = ThermometerState.Cooling
        else:
            self.state = ThermometerState.Comfortable


    def SetState(self, state):
        if state >= 0 and state < numberOfThermometerStates:
            self.state = state

    def GetState(self):
        return self.state

    def SetTempurature(self, tmp):
        self.tempurature = tmp
 
    def GetTempurature(self):
        return self.tempurature

    def FanOn(self):
        self.SetState(ThermometerState.Fan)

    def TurnOff(self):
        self.SetState(ThermometerState.Off)

    def TurnOn(self):
        self.SetState(ThermometerState.Undefined)

