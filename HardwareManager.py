from DebuggingControl import Debug

try:
    import RPi.GPIO as GPIO
except ImportError:
    Debug(True)
    print("Debugging Mode Active")


class ModelHardware():
    def __init__(self, HWM, master):
        tkinter.Frame.__init__(master)
        self.master = master
        self.grid()
        self.HWM = HWM
    
        avgLabel = tkinter.Label(self, text="Cool: ")
        avgLabel.grid(column=0, row=0)
        lowestLabel = tkinter.Label(self, text="Fan: ")
        lowestLabel.grid(column=0, row=7)
        highestLabel = tkinter.Label(self, text="Hot: ")
        highestLabel.grid(column=0, row=6)
        
        self.currentTempurature = tkinter.Label(self, text="0")
        self.currentTempurature.grid(column=1, row=0)
        self.lowestTempurature = tkinter.Label(self, text="0")
        self.lowestTempurature.grid(column=1, row=7)
        self.highestTempurature = tkinter.Label(self, text="0")
        self.highestTempurature.grid(column=1, row=6)
        
        self.after(1000, self.UpdateLabels)

    def UpdateLabels(self):
        self.currentTempurature['text'] = "%.2f" % self.ctrlLogic.GetAverageTempurature()
        self.lowestTempurature['text'] = "%.2f" % self.ctrlLogic.GetLowestTempurature()
        self.highestTempurature['text'] = "%.2f" % self.ctrlLogic.GetHighestTempurature()
        self.currentState['text'] = CL.ThermometerState.GetStateText(self.ctrlLogic.GetState())
        self.sensorCount['text'] = str(self.ctrlLogic.GetValidSensorCount())
        self.lowSetting['text'] = str(self.tempuratureControl.GetCoolLimit())
        self.highSetting['text'] = str(self.tempuratureControl.GetHeatLimit())

        self.after(500, self.UpdateLabels)
        
class RelayLine():
    def __init__(self, GPIO_out):
        self.active = False
        self.discrete = GPIO_out
        GPIO.setup(GPIO_out, GPIO.OUT)

    def isActive(self):
        return self.active

    def setActive(self, active):
        self.active = active
        self.Operate()

    def getDiscrete(self):
        return self.discrete

    def Operate(self):
        if self.isActive():
            GPIO.output(self.getDiscrete(), 1)
        else:
            GPIO.output(self.getDiscrete(), 0)

    def CleanUp(self):
        GPIO.cleanup()
        
class ModelRelayLine(RelayLine):
    def __init__(self, GPIO_out):
        self.active = False
        self.discrete = GPIO_out
        
    def Operate(self):
        pass

    def CleanUp(self):
        pass
        
class HardwareManager():
    def __init__(self):
        debug = Debug()
        if debug:
            self.Cool = ModelRelayLine(24)
            self.Heat = ModelRelayLine(23)
            self.Fan = ModelRelayLine(18)
            
        else:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            self.Cool = RelayLine(24)
            self.Heat = RelayLine(23)
            self.Fan = RelayLine(18)

    def StartCool(self):
        self.Cool.setActive(True)
        self.Fan.setActive(True)
        self.Heat.setActive(False)

    def StartHeat(self):
        self.Cool.setActive(False)
        self.Fan.setActive(True)
        self.Heat.setActive(True)


    def StartFan(self):
        self.Cool.setActive(False)
        self.Fan.setActive(True)
        self.Heat.setActive(False)
        
    def Off(self):
        self.Cool.setActive(False)
        self.Fan.setActive(False)
        self.Heat.setActive(False)        
        
    def DoCleanUp(self):
        self.Cool.CleanUp()
        self.Fan.CleanUp()
        self.Heat.CleanUp()        

        


