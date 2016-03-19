
import TempuratureHardwareManager as THM
import TempuratureMeter as TM

class ThermometerState():
    Undefined, Comfortable, Heating, Cooling = range(4)

class TempuratureControlLogic():
    def __init__(self, Cold = 70, Hot = 74):
        self.state = ThermometerState.Undefined
        self.tempurature = None
        self.hardware = THM.TempuratureHardwareManager()
        self.tempurature_control = TM.TempuratureControl(Cold, Hot)

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
        if self.tempurature <= self.tempurature_control.getCoolLimit() + differential:
            self.state = ThermometerState.Heating
        elif self.tempurature >= self.tempurature_control.getHeatLimit() + differential:
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

