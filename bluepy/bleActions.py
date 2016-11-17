import binascii
import struct
import time
from btle import UUID, Peripheral

class bleActions:
    # Reads a specified characeristic of a given device mac
    @staticmethod
    def read_characteristic(device_mac, char_num): #(String, int)

        curr_uuid = UUID(char_num)
        peripheral = Peripheral(device_mac, "random")

        try:
            characteristic = peripheral.getCharacteristics(uuid=curr_uuid)[0]
            if (characteristic.supportsRead()):
                while(1):
                    val = binascii.b2a_hex(characteristic.read())
                    val = binascii.unhexify(val)
                    print str(val)
                    time.sleep(1)

        finally:
            peripheral.disconnect()

    # Reads a single value from a characteristic of a peripheral
    @staticmethod
    def read_characteristic_from_device(peripheral, char_num): #(Periph, int)

        curr_uuid = UUID(char_num)
        
        try:
            characteristic = peripheral.getCharacteristics(uuid=curr_uuid)[0]
            if (characteristic.supportsRead()):
                val = binascii.b2a_hex(characteristic.read())
                val = binascii.unhexify(val)
                return val

        except:
            return "ERROR: Read error"

    # Retrieves all characteristics from a device
    @staticmethod
    def retrive_characteristics_from_device(peripheral): #(Peripheral)

        characteristic_list = []
        
        for svc in peripheral.getServices():
            for ch in scv.getCharacteristics():
                characteristic_list.append(ch)

        return characteristic_list

    # Retrieve readable characteristics from device
    @staticmethod
    def retrieve_readable_characteristics(peripheral): #(Peripheral)

        readable_characteristic_list = []

        for svc in peripheral.getServices():
            for ch in svc.getCharacteristics():
                if (ch.supportsRead()):
                    readable_characteristic_list.append(ch)

        return readable_characteristic_list

    
