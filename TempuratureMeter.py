
# TODO Add functionality to check for phones on the wifi; adjust tempurature accordingly

class TempuratureMeter():
    def __init__(self, Cold = 70, Hot = 74):
        self.coolLimit = Cold
        self.heatLimit = Hot
        self.MaxHot = 100
        self.MinCool = 50
        self.MinDifference = 2

    def getHeatLimit(self):
        return self.heatLimit

    def getCoolLimit(self):
        return self.coolLimit

    def matchCoolLimit(self):
        self.heatLimit = self.coolLimit + self.MinDifference

    def matchHeatLimit(self):
        self.coolLimit = self.heatLimit - self.MinDifference

    def decreaseCoolLimit(self, amount=1):
        if self.coolLimit-amount >= self.MinCool:
            self.coolLimit-=amount
        else:
            self.coolLimit = self.MinCool

    def increaseCoolLimit(self, amount=1):
        if self.coolLimit+amount < self.MaxHeat-self.MinDifference:
            self.coolLimit+=amount
        else:
            self.coolLimit = self.MaxHeat-self.MinDifference

        if self.coolLimit+self.MinDiffernce > self.heatLimit:
            self.matchCoolLimit()

    def increaseHeatLimit(self, amount=1):
        if self.heatLimit+amount <= self.MaxHeat:
            self.heatLimit+=amount
        else:
            self.heatLimit = self.MaxHeat

    def decreaseHeatLimit(self, amount=1):
        if self.coolLimit-amount < self.MinCool+self.MinDifference:
            self.coolLimit-=amount
        else:
            self.coolLimit = self.MaxHot+self.MinDifference

        if self.heatLimit < self.coolLimit+self.MinDifference:
            self.matchHeatLimit()
        
