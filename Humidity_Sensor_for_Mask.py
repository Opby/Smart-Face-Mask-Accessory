from bluepy.btle import *
from requests.exceptions import ConnectionError, ReadTimeout
import sys
import time
from pygame import mixer      

def scan(currentstate):
    scanner = Scanner(0)
    devices = scanner.scan(3) # List of ScanEntry objects
    connected = False
    ble = None
    triggered = False
    mixer.init()
    mixer.music.load("./1.mp3")
    mixer.music.play()
    filename = time.strftime("%Y%m%d_%H%M%S")
    if currentstate == '0':
        f = open("output/" + "sense1_" + filename + "_waittoturnon.csv", "w")
    else:
        f = open("output/" + "sense1_" + filename + "_waittoturnoff.csv", "w")
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
                                print("****************connected*************")
                                services = ble.getServices()
                            characteristics = ble.getCharacteristics()
                            f.write(time.strftime("%Y%m%d_%H%M%S") + ",")
                            for k in characteristics:
                                if k.uuid=="2a6f":
                                    humidity_data = k.read()
                                    calcHum = ((ord(humidity_data[1])<<8)+ord(humidity_data[0]))/100.
                                    print ("current humidity is: ", calcHum)
                                    f.write(str(calcHum) + ",")
                                    if calcHum > 45. and currentstate == '0':
                                        triggered = True
                                    elif calcHum <= 45. and currentstate == '1':
                                        triggered = True
                            f.flush()
                           # if triggered:
                           #     ble.disconnect()
                           #     return True
                            time.sleep(1)
        except:
            connected = False
    f.close()
    return False

scan(0)
