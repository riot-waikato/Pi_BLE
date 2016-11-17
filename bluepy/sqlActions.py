import binascii
import struct
import time
import subprocess

class sqlActions:
    database_name = 'tester2.db'
    
    # add motion entry
    @staticmethod
    def insert_motion(device_id, time_stamp, data):

        if len(data) != 9:
            print "Data length not equal to 9"
            return "Data length Error"

        curr_time = str(int(time.time()))
        data_line = data[0] + " " + data[1] + " " + data[2]
                    + data[3] + " " + data[4] + " " + data[5]
                    + data[6] + " " + data[7] + " " + data[8]

        result = subprocess.call(['./Add_motion.sh ' + database_name + ' ' + device_id + ' ' + curr_time + ' ' + data_line])
