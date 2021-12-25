# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:00:54 2021

@author: imjprojts
This file creates a log.csv in the same folder that contains data from the OBD port
"""
#import bluetooth
import obd

from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
import time
import sys
#import logging
import csv
#import os

global writcsv
global arr
arr=[]

csvfile = open('log.csv', 'a', newline='')
writcsv = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
writcsv.writerow(['RPM', 'B+', 'm1v', 'm2v', 'm3v', 'm4v', 'm5v', 'm6v', 'm7v', 'm8v', 'm9v', 'm10v' ])

#os.system('sudo rfcomm connect hci0 00:1D:A5:20:17:AD 1')
#os.system("sudo sdptool add SP")				# set up serial port using linux's sdptool
#time.sleep(5)							# sdptool returns before port fully set up? so wait a jiff
#os.system("sudo rfcomm connect hci0 AA:BB:CC:11:22:33 1 &")	# connect using OBD2 unit's mac address. rfcomm locks, so detach(using "&")
#time.sleep(5)	

#PORT=/dev/rfcomm0
#BAUD = 38400
#PROTOCOL = 6
#ECU = 0 ENGINE
#ECU = 2 UNKNOWN

#logging
#obd.logger.setLevel(obd.logging.DEBUG)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

#silence logging
#obd.logger.removeHandler(obd.console_handler)

#log = open("output.txt", "a")  # append mode

def rpm(messages):
    """ decoder for RPM messages """
    global arr
    rp = messages[0].data
    print(rp)
    rpm = ((rp[11]*256+rp[12])/4) 
    arr.append(rpm)
    print (f'Engine RPM{rpm}')
    return rpm # construct a Pint Quantity
def bvolt(messages):
    """ decoder for 12v battery voltage messages """
    global arr
    bv = messages[0].data
    print(bv)
    voltage = (bv[0]/10) 
    arr.append(voltage)
    print (f'12v Battery voltage{voltage}')
    return voltage # construct a Pint Quantity
def b2volt(messages):
    """ decoder for 12v battery voltage messages """
    global arr
    bv = messages[0].data
    print(bv)
    voltage = ((bv[2]*256+bv[3])/1000)  
    arr.append(voltage)
    print (f'12v Battery voltage{voltage}')
    return voltage # construct a Pint Quantity
def modvolt(messages):
    """ decoder for module voltage messages """
    global writcsv
    global arr
    modv = messages[0].data

    v1 = ((modv[2]*256+modv[3])/1000) 
    v2 = ((modv[4]*256+modv[5])/1000) 
    v3 = ((modv[6]*256+modv[7])/1000)  
    v4 = ((modv[8]*256+modv[9])/1000)
    v5 = ((modv[10]*256+modv[11])/1000)
    v6 = ((modv[12]*256+modv[13])/1000)
    v7 = ((modv[14]*256+modv[15])/1000)
    v8 = ((modv[16]*256+modv[17])/1000)
    v9 = ((modv[18]*256+modv[19])/1000)
    v10 = ((modv[20]*256+modv[21])/1000)
    arr.append(v1)
    arr.append(v2)
    arr.append(v3)
    arr.append(v4)
    arr.append(v5)
    arr.append(v6)
    arr.append(v7)
    arr.append(v8)
    arr.append(v9)
    arr.append(v10)
    writcsv.writerow(arr)
    arr=[]

    print (f'Module 1 voltage{v1}')
    print (f'Module 2 voltage{v2}')
    print (f'Module 3 voltage{v3}')
    print (f'Module 4 voltage{v4}')
    print (f'Module 5 voltage{v5}')
    print (f'Module 6 voltage{v6}')
    print (f'Module 7 voltage{v7}')
    print (f'Module 8 voltage{v8}')
    print (f'Module 9 voltage{v9}')
    print (f'Module 10 voltage{v10}')

    return v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 # construct a Pint Quantity

def modEsr(messages):
    """ decoder for module voltage messages """
    global writcsv
    global arr
    modr = messages[0].data

    c1 = (modr[2]/1000) 
    c2 = (modr[3]/1000) 
    c3 = (modr[4]/1000)  
    c4 = (modr[5]/1000)
    c5 = (modr[6]/1000)
    c6 = (modr[7]/1000)
    c7 = (modr[8]/1000)
    c8 = (modr[8]/1000)
    c9 = (modr[10]/1000)
    c10 = (modr[11]/1000)
    arr.append(c1)
    arr.append(c2)
    arr.append(c3)
    arr.append(c4)
    arr.append(c5)
    arr.append(c6)
    arr.append(c7)
    arr.append(c8)
    arr.append(c9)
    arr.append(c10)
    writcsv.writerow(arr)
    arr=[]

    print (f'Module 1 voltage{c1}')
    print (f'Module 2 voltage{c2}')
    print (f'Module 3 voltage{c3}')
    print (f'Module 4 voltage{c4}')
    print (f'Module 5 voltage{c5}')
    print (f'Module 6 voltage{c6}')
    print (f'Module 7 voltage{c7}')
    print (f'Module 8 voltage{c8}')
    print (f'Module 9 voltage{c9}')
    print (f'Module 10 voltage{c10}')

    return c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 # construct a Pint Quantity

#cmd = obd.commands.RPM # select an OBD command (sensor)
crpm = OBDCommand("RPM",         # name
                 "Engine RPM",   # description
                 #b"010C",        # command
                 b"2101",        # command
                 27,              # number of return bytes
                 rpm,            # decoding function
                 ECU.ENGINE,     # (optional) ECU filter
                 True)             # (optional) enable optimizations

cbv = OBDCommand("BV",         # name
                 "12V Battery voltage",   # description
                 b"2113",        # command
                 3,              # number of return bytes
                 bvolt,            # decoding function
                 ECU.ALL,     # (optional) ECU filter
                 True)             # (optional) enable optimizations

cbv2 = OBDCommand("BV2",         # name
                 "12V Battery voltage",   # description
                 b"0142",        # command
                 2,              # number of return bytes
                 b2volt,            # decoding function
                 ECU.ALL,     # (optional) ECU filter
                 True)             # (optional) enable optimizations

cmv = OBDCommand("MV",         # name
                 "Module Voltages",   # description
                 b"2181",        # command
                 26,              # number of return bytes
                 modvolt,            # decoding function
                 #ECU.ALL,     # (optional) ECU filter
                 True, # (optional) enable optimizations
                 700) #header       

cmesr = OBDCommand("MESR",         # name
                 "Module Internal Resistance",   # description
                 b"2195",        # command
                 12,              # number of return bytes
                 modEsr,            # decoding function
                 #ECU.ALL,     # (optional) ECU filter
                 True, # (optional) enable optimizations
                 700) #header       


#obd.supported_commands.add(cmv)  #remove the messave "WARNING:obd.obd:'b'2181': Module Voltages' is not supported"

# will continuously print new RPM values
def new_rpm(response):
    #log.write(str(response.value))
    print("RPM", str(response.value))
def new_BV(response):
    #log.write(str(response.value))
    print("12v Bat V", str(response.value))
def new_B2V(response):
    #log.write(str(response.value))
    print("12v Bat V2", str(response.value))
def new_MV(response):
    #log.write(str(response.value))
    print("Drive Bat Vs", str(response.value))
def new_MESR(response):
    #log.write(str(response.value))
    print("Drive Bat ESRs", str(response.value))

#connection = obd.OBD() # auto-connects to USB or RF port
#connection = obd.Async(portstr=("/dev/rfcomm0"), baudrate=(38400), protocol=(6)) # create an asynchronous connection
connection = obd.Async()
connection.supported_commands.add(crpm)
connection.supported_commands.add(cmv)
connection.supported_commands.add(cbv)
connection.supported_commands.add(cbv2)
connection.supported_commands.add(cmesr)
#response = connection.query(cmd) # send the command
#print(response) # "2410 RPM"

# keep track of some PIDs
connection.watch(crpm, callback=new_rpm)
connection.watch(cbv, callback=new_BV)
connection.watch(cbv2, callback=new_B2V)
connection.watch(cmv, callback=new_MV)
connection.watch(cmesr, callback=new_MESR)
connection.start()
time.sleep(60) # do other work in the main thread
connection.stop()
#sys.stdout.close()
csvfile.close()

"""
$5C is the standard PID.
$7E0 is the non standard PID.
AT SH 7E0 - sets the header to $7E0
2101 - requests mode $21 PID $01

Should get a response with 7E8 and /X/ bytes of data behind it, 
which you should then be able to decode.
01F 0: 61 01 00 00 00 00 1: 55 66 54 45 5 5A 00 2: 00 00 00 00 0C 29 53 3: 21 21 00 3D 05 AD 09 4: 42 30 04 58 00 00 00 SEARCHI
01F
0: 61 01 00 00 00 00
1: 55 66 54 45 5 5A 00
2: 00 00 00 00 0C 29 53
3: 21 21 00 3D 05 AD 09
4: 42 30 04 58 00 00 00 
SEARCHI
01F = 31, which means to expect a 31 byte response
AT SP0 set the header back to auto/search???
OBD2 Mode and PID: 2101
Minimum Value: -40
Maximum Value: 215 (this is just the maximum that this location can support, which does not mean the sensor can read that high)
Scale factor: x1
Unit type: C
Equation: AC-40 (no space between A and C; "AC" is the location within the response)
OBD Header: 7E0 (Auto also works, but seems to take longer)
"""
