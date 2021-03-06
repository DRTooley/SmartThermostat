
from ExternalDeviceSearch import DeviceSearch


class TempuratureMeter():
    def __init__(self, Cold = 70, Hot = 73):
        self.coolLimit = Cold
        self.heatLimit = Hot
        self.maxHeat = 100
        self.minCool = 50
        self.minDifference = 3
        self.unoccupiedAdjustment = 3
        self.device = DeviceSearch()
        self.MatchCoolLimit()
        self.CheckBounds()

    def CheckBounds(self):
        if self.heatLimit > self.maxHeat:
            self.coolLimit = self.maxHeat-self.minDifference
            self.heatLimit = self.maxHeat

        if self.coolLimit < self.minCool:
            self.heatLimit = self.minCool+self.minDifference
            self.coolLimit = self.minCool

    def GetHeatLimit(self):
        if self.device.deviceFound:
            return self.heatLimit
        else:
            return self.heatLimit + self.unoccupiedAdjustment

    def GetCoolLimit(self):
        if self.device.deviceFound:
            return self.coolLimit
        else:
            return self.coolLimit + self.unoccupiedAdjustment

    def MatchCoolLimit(self):
        if self.coolLimit+self.minDifference > self.heatLimit:
            self.heatLimit = self.coolLimit + self.minDifference

    def MatchHeatLimit(self):
        if self.heatLimit < self.coolLimit+self.minDifference:
            self.coolLimit = self.heatLimit - self.minDifference

    def DecreaseCoolLimit(self, amount=1):
        if self.coolLimit-amount >= self.minCool:
            self.coolLimit-=amount
        else:
            self.coolLimit = self.minCool

    def IncreaseCoolLimit(self, amount=1):
        self.coolLimit+=amount
        self.MatchCoolLimit()
        self.CheckBounds()

    def IncreaseHeatLimit(self, amount=1):
        if self.heatLimit+amount <= self.maxHeat:
            self.heatLimit+=amount
        else:
            self.heatLimit = self.maxHeat

    def DecreaseHeatLimit(self, amount=1):
        self.heatLimit-=amount
        self.MatchHeatLimit()
        self.CheckBounds()


        
