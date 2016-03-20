import tkinter
import threading
import ControlLogic as CL
import ThreadTimeValidator as TTV
import TempuratureMeter as TM


class ThermostatApp(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.tempuratureControl = TM.TempuratureMeter()
        self.threadValidator = TTV.ThreadTimeValidator()
        self.ctrlLogic = CL.ControlLogic(self.threadValidator, self.tempuratureControl)

        self.Initialize()


    def Initialize(self):
        self.grid()

        avgLabel = tkinter.Label(self, text="Average: ")
        avgLabel.grid(column=0, row=0)
        lowestLabel = tkinter.Label(self, text="Lowest: ")
        lowestLabel.grid(column=0, row=7)
        highestLabel = tkinter.Label(self, text="Highest: ")
        highestLabel.grid(column=0, row=6)
        stateLabel = tkinter.Label(self, text="State: ")
        stateLabel.grid(column=0, row=9)
        
        self.currentTempurature = tkinter.Label(self, text="TBD")
        self.currentTempurature.grid(column=1, row=0)
        self.lowestTempurature = tkinter.Label(self, text="TBD")
        self.lowestTempurature.grid(column=1, row=7)
        self.highestTempurature = tkinter.Label(self, text="TBD")
        self.highestTempurature.grid(column=1, row=6)
        self.currentState = tkinter.Label(self, text="Undefined")
        self.currentState.grid(column=1, row=9)


        lowSettingLabel = tkinter.Label(self, text="Low Setting:   ")
        lowSettingLabel.grid(column=3, row=2)
        highSettingLabel = tkinter.Label(self, text="High Setting: ")
        highSettingLabel.grid(column=3, row=1)

        self.lowSetting = tkinter.Label(self, text="71")
        self.lowSetting.grid(column=4, row=2)
        self.highSetting = tkinter.Label(self, text="73")
        self.highSetting.grid(column=4, row=1)

        validSensorCountLabel = tkinter.Label(self, text="# Valid Sensors:   ")
        validSensorCountLabel.grid(column=0, row=5)
        self.sensorCount = tkinter.Label(self, text="TBD")
        self.sensorCount.grid(column=1, row=5)


        tempUpButton = tkinter.Button(self, text="Temp Up!", command=self.IncreaseTempurature)
        tempUpButton.grid(column=6, row=0)

        tempDownButton = tkinter.Button(self, text="Temp Down!", command=self.DecreaseTempurature)
        tempDownButton.grid(column=6, row=2)

        fanOnlyButton = tkinter.Button(self, text="Fan Only!", command=self.StartFan)
        fanOnlyButton.grid(column=8, row=0)

        turnOffButton = tkinter.Button(self, text="Turn Off!", command=self.TurnOff)
        turnOffButton.grid(column=10, row=0)

        turnOnButton = tkinter.Button(self, text="Turn On!", command=self.TurnOn)
        turnOnButton.grid(column=10, row=2)

        quitButton = tkinter.Button(self, text="Quit!", command=self.Quit)
        quitButton.grid(column=10, row=10)

        self.UpdateLabels()

    def UpdateLabels(self):
        self.currentTempurature['text'] = "%.2f" % self.ctrlLogic.GetAverageTempurature()
        self.lowestTempurature['text'] = "%.2f" % self.ctrlLogic.GetLowestTempurature()
        self.highestTempurature['text'] = "%.2f" % self.ctrlLogic.GetHighestTempurature()
        self.currentState['text'] = CL.ThermometerState.GetStateText(self.ctrlLogic.GetState())
        self.sensorCount['text'] = str(self.ctrlLogic.GetValidSensorCount())
        self.lowSetting['text'] = str(self.tempuratureControl.GetCoolLimit())
        self.highSetting['text'] = str(self.tempuratureControl.GetHeatLimit())

        if self.threadValidator.isRunning():
            waitTime = self.threadValidator.GetUpdateDisplayWaitTime()
            threading.Timer(waitTime, self.UpdateLabels).start()


    def Quit(self):
        self.threadValidator.Exit()
        self.ctrlLogic.TurnOff()

    def StartFan(self):
        self.ctrlLogic.FanOn()

    def TurnOff(self):
        self.ctrlLogic.TurnOff()

    def TurnOn(self):
        self.ctrlLogic.TurnOn()

    def IncreaseTempurature(self):
        self.tempuratureControl.IncreaseCoolLimit()

    def DecreaseTempurature(self):
        self.tempuratureControl.DecreaseHeatLimit()

