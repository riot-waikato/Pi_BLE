import time
from btle import Scanner, DefaultDelegate, Peripheral, UUID, Service, Characteristic
import bleActions

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print "Discovered ", dev.addr
        elif isNewData:
            print "Received ", dev.addr


SERV_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
TX_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
RX_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
            
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(15.0)

URT_devices = []

for dev in devices:
    device_scan_data = dev.getScanData()
    last_tuple =  device_scan_data[-1]
    last_item = last_tuple[-1]
    last_item.encode("ascii")
    if last_item == 'URT':
        print "URT ", dev.addr, " ", dev.addrType
        URT_devices.append(Peripheral(dev.addr, dev.addrType))

while(1):
    for device in URT_devices:
        #serv_service = device.getServiceByUUID(SERV_UUID)
        #tx_service = device.getServiceByUUID(TX_UUID)
        chars = device.getCharacteristics()
        for ch in chars:
            if ch.supportsRead():
                try:
                    print ch.read()
                except:
                    print "GAP IN TRANSMISSION"
#while(1):
#    for dev in devices:
#        print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi)
#        for (adtype, desc, value) in dev.getScanData():
#            print "  %s = %s" % (desc, value)
