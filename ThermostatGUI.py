import tkinter
import ControlLogic as CL
import ThreadTimeValidator as TTV
import TempuratureMeter as TM


class ThermostatApp(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.Initialize()
        self.tempuratureControl = TM.TempuratureMeter()
        self.threadValidator = TTV.ThreadTimeValidator()
        self.ctrlLogic = CL.ControlLogic(self.threadValidator, self.tempuratureControl)

    def Initialize(self):
        self.grid()

        tempUpButton = tkinter.Button(self, text="Temp Up!", command=self.IncreaseTempurature)
        tempUpButton.grid(column=4, row=0)

        tempDownButton = tkinter.Button(self, text="Temp Down!", command=self.DecreaseTempurature)
        tempDownButton.grid(column=4, row=2)


        turnOffButton = tkinter.Button(self, text="Turn Off!", command=self.TurnOff)
        turnOffButton.grid(column=2, row=0)

        turnOnButton = tkinter.Button(self, text="Turn On!", command=self.TurnOn)
        turnOnButton.grid(column=2, row=2)

        fanOnlyButton = tkinter.Button(self, text="Fan Only!", command=self.StartFan)
        fanOnlyButton.grid(column=1, row=0)


        quitButton = tkinter.Button(self, text="Quit!", command=self.Quit)
        quitButton.grid(column=0, row=5)


    def Quit(self):
        self.threadValidator.Exit()
        self.ctrlLogic.TurnOff()
        print("Quitting!")

    def StartFan(self):
        self.ctrlLogic.FanOn()

    def TurnOff(self):
        self.ctrlLogic.TurnOff()

    def TurnOn(self):
        self.ctrlLogic.TurnOn()

    def IncreaseTempurature(self):
        self.tempuratureControl.IncreaseCoolLimit()
        self.PrintCurrentLimits()

    def DecreaseTempurature(self):
        self.tempuratureControl.DecreaseHeatLimit()
        self.PrintCurrentLimits()

    def PrintCurrentLimits(self):
        print("New Heat Limit:  "+ str(self.tempuratureControl.GetHeatLimit()))
        print("New Cool Limit:  "+ str(self.tempuratureControl.GetCoolLimit()))
