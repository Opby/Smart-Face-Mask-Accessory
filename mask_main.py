import sys
import os
import time
from bluepy.btle import *
from requests.exceptions import ConnectionError, ReadTimeout

def mask_control():
    scanner = Scanner(0)
    devices = scanner.scan(3) # List of ScanEntry objects
    connected = False
    ble = None
    speakeron = False
    while True:
        if connected == False:
            scanner = Scanner(0)
            devices = scanner.scan(3)  # List of ScanEntry objects
        try:
            for dev in devices:
                for (adtype, desc, value) in dev.getScanData():
                     if "Thunder Sense" in value:
                        print("addr {}, addrtype {}, value {}".format(dev.addr, dev.addrType, value))
                    
                        if connected == False:
                            ble = Peripheral()
                            ble.connect('58:8e:81:72:f9:dd','public')
                            connected = True
                            print("Humidity Sensor Active")
                            services = ble.getServices()
                        characteristics = ble.getCharacteristics()
                        print("here")
                        for k in characteristics:
                            if k.uuid=="2a6f":
                                humidity_data = k.read()
                                calcHum = ((ord(humidity_data[1])<<8)+ord(humidity_data[0]))/100.
                                print ("current humidity is: ", calcHum)
                                if calcHum > 45. :
                                    speakeron = True
                                    print("speakeron true")
                                    os.system("sudo arecord -f cd -Dhw:2 | aplay -Dhw:2")
                                elif calcHum <= 45. :
                                    speakeron = False
                                    print("speakeron false")
                        time.sleep(1)
        except:
            connected = False
    return False

mask_control()