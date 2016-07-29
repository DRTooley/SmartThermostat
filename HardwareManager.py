from DebuggingControl import Debug

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Debugging Mode Active")
    Debug(True)

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
        d = Debug()
        if d.GetInfo():
            print("Model Active")
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

        


