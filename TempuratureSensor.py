
import threading

class TempuratureSensor():
    def __init__(self,file_location, ThreadTimes):
        self.file_location = file_location
        self.tempurature_reading = None
        self.tempurature_valid = False
        self.running = True
        self.threadValidator = ThreadTimes

        self.StartUpdate()

    def StartUpdate(self):
        if self.threadValidator.isRunning():
            waitTime = self.threadValidator.GetSensorUpdateWaitTime()
            t = threading.Timer(waitTime, self.Update).start()       
            self.threadValidator.SetSensorUpdateTimerThread(t)

    def Update(self):
        temp = 0
        split = None
        try:
            with open(self.file_location, 'r') as tempfile:
                lines = tempfile.read()
                split = lines.split()
                temp = split[-1]
                temp = temp[2:]
        except IOError:
            self.tempurature_reading = None
            self.tempurature_valid = False
            self.running = False

        else:
            if split[11] == 'YES':
                self.tempurature_reading = int(temp)/1000 * 9/5 + 32

                # This check is implemented to protect against errant tempurature sensor data
                # In the event the sensor loses +3.3V it will report "YES" but give 0 degree Celcius 
                # This would be a very bad value to take into the average calcluation
                # Similarly if the comm wire is removed it could report 185 degrees Fahrenheit. Also bad.
                # To protect against these known issues and other potential unkowns I have bound the reading
                # to what I consider to be valid upper and lower bounds.
                if self.tempurature_reading >= 130 or self.tempurature_reading <= 45:
                    self.tempurature_reading = None
                    self.tempurature_valid = False
                else:
                    self.tempurature_valid = True

            else:
                self.tempurature_reading = None
                self.tempurature_valid = False
                
            self.StartUpdate()


            

    def getTempurature(self):
        return self.tempurature_reading

    def getTempuratureValid(self):
        return self.tempurature_valid

    def getFileLocation(self):
        return self.file_location

    def isRunning(self):
        return self.running
        
