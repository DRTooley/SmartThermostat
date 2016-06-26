import subprocess
import threading
import time

class DeviceSearch():
    def __init__(self):
        self.MAC_Addresses = [
            'fc:db:b3:43:47:08',
            '5c:8d:4e:cf:7c:82'
        ]

        self.deviceFound = True

        t = threading.Thread(target=self.DeviceSearch)
        t.daemon = True
        t.start()

    def DeviceSearch(self):
        while True:
            deviceConnected = False
            MAC_Search = ''
            MAC_Search = MAC_Search [:-1]
            p = subprocess.Popen("arp-scan -l", stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()
            for MAC in self.MAC_Addresses:
                if MAC in output.decode():
                    print("Found")
                    deviceConnected = True
                else:
                    print("Not Found {}".format(MAC))
                    print(output.decode())
            self.deviceFound = deviceConnected
            time.sleep(5)

        
