import subprocess
import threading
import time

class DeviceSearch():
    def __init__(self):
        self.MAC_Addresses = [
            'fc:db:b3:43:47:08',
            '5c:8d:4e:cf:7c:82'
        ]
        self.IP_Addresses = [
            '192.168.1.200',
            '192.168.1.201'
        ]

        self.deviceFound = True

        t = threading.Thread(target=self.DeviceSearch)
        t.daemon = True
        t.start()

    def DeviceSearch(self):
        while True:
            deviceConnected = False
            for IP in self.IP_Addresses:
                p = subprocess.Popen(["ping", '-c', '2', IP],
                                     stdout=subprocess.PIPE, shell=False)
                (output, err) = p.communicate()
                p_status = p.wait()
                if "Host Unreachable" not in output.decode():
                    print("Found")
                    print(output.decode())
                    deviceConnected = True
                else:
                    print("Not Found {}".format(IP))
                    print(output.decode())
            self.deviceFound = deviceConnected
            print(self.deviceFound)
            time.sleep(30)

        
