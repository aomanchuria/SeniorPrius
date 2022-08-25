# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:00:54 2021

@author: imjprojts
This file creates a log.csv in the same folder that contains data from the OBD port
"""
#import bluetooth
import numpy as np
import obd
import time
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.protocols import ECU_HEADER
from obd.utils import bytes_to_int
import time
import sys
import csv


global writcsv, timestr
global idx
global dat
global arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2
timestr = time.strftime("%Y%m%d-%H%M%S")
timestr = timestr + ".csv"
arr=[]
Row_lines =[]


idx=0


csvfile = open(timestr, 'a', newline='')
writcsv = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

arr_ENG1=np.array(['RPM'])
arr_BV=np.array(['B+'])
arr_B2V=np.array(['B2+'])
arr_MV=np.array(['m1v', 'm2v', 'm3v', 'm4v', 'm5v', 'm6v', 'm7v', 'm8v', 'm9v', 'm10v'])
arr_MESR=np.array(['m1r', 'm2r', 'm3r', 'm4r', 'm5r', 'm6r', 'm7r', 'm8r', 'm9r', 'm10r'])
arr_MTMP=np.array(['bt1', 'bt2', 'bt3','bt4'])
arr_ENG2=np.array(['eng2Load', 'eng2Map', 'eng2Iat', 'eng2At', 'eng2Ap', 'eng2cTmp', 
        'eng2rpm', 'eng2vsp', 'eng2ert', 'eng2tp', 'eng2ap1', 'eng2ap2', 
        'eng2dtcw', 'eng2dtcd', 'eng2dtct', 'eng2bp', 'eng2soc'])

dat = np.concatenate((arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2))

writcsv.writerow(dat) #write to CSV after all row data has been collected


#sudo rfcomm bind /dev/rfcomm0 hci0 AA:BB:CC:11:22:33 1
#os.system('sudo rfcomm connect hci0 AA:BB:CC:11:22:33 1')
#os.system("sudo sdptool add SP")				# set up serial port using linux's sdptool
#time.sleep(5)							# sdptool returns before port fully set up? so wait a jiff
#os.system("sudo rfcomm connect hci0 AA:BB:CC:11:22:33 1 &")	# connect using OBD2 unit's mac address. rfcomm locks, so detach(using "&")
#time.sleep(5)	

#Prius C 2014 reports these, but sending direct connect commad did not work with these values
#PORT=/dev/rfcomm0
#BAUD = 38400
#PROTOCOL = 6
#ECU = 0 ENGINE
#ECU = 2 UNKNOWN

#logging
#obd.logger.setLevel(obd.logging.DEBUG)
#no logging
obd.logger.removeHandler(obd.console_handler)
#logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

#silence logging
#obd.logger.removeHandler(obd.console_handler)

#log = open("output.txt", "a")  # append mode

#########
#define headers found in Prius C
ECU_HEADER.MY=b'7E2'
ECU_HEADER.PCH7=b'7E2'
ECU_HEADER.PCH700=b'7E2'
ECU_HEADER.PCH7B0=b'7B0'
ECU_HEADER.PCH7C0=b'7C0'
ECU_HEADER.PCH7C4=b'7C4'
#########


#########
#Decoding Functions
#########

def eng1(messages):
    """Decode various Engine messages."""
    #global arr
    msg = messages[0].data
    #print(msg)
    rpm = ((msg[11]*256+msg[12])/4) 
    #arr.append(rpm)
    #print (f'Engine RPM{rpm}')
    return rpm # construct a Pint Quantity

def bvolt(messages):
    """Decode 12v battery voltage messages."""
    #global arr
    bv = messages[0].data
    #print(bv)
    voltage = (bv[2]/10) 
    #arr.append(voltage)
    #print (f'12v Battery voltage{voltage}')
    return voltage # construct a Pint Quantity

def b2volt(messages):
    """Decode 12v battery voltage messages."""
    #global arr
    bv = messages[0].data
    #print(bv)
    voltage = ((bv[2]*256+bv[3])/1000)  
    #arr.append(voltage)
    #print (f'12v Battery voltage{voltage}')
    return voltage # construct a Pint Quantity

def modvolt(messages):
    """Decode module voltage messages."""
    #global arr
    modv = messages[0].data
    v1 = str((modv[2]*256+modv[3])/1000) 
    v2 = str((modv[4]*256+modv[5])/1000) 
    v3 = str((modv[6]*256+modv[7])/1000)  
    v4 = str((modv[8]*256+modv[9])/1000)
    v5 = str((modv[10]*256+modv[11])/1000)
    v6 = str((modv[12]*256+modv[13])/1000)
    v7 = str((modv[14]*256+modv[15])/1000)
    v8 = str((modv[16]*256+modv[17])/1000)
    v9 = str((modv[18]*256+modv[19])/1000)
    v10 = str((modv[20]*256+modv[21])/1000)
    return v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 

def modEsr(messages):
    """Decode module internal resistance."""
    #global arr
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
    return c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 

def modTmp(messages):
    """Decode module temperature messages."""
    #global arr
    modv = messages[0].data

    bt1 = ((modv[2]*256+modv[3])*255.9/65535-50)
    bt2 = ((modv[4]*256+modv[5])*255.9/65535-50)
    bt3 = ((modv[6]*256+modv[7])*255.9/65535-50) 
    bt4 = ((modv[8]*256+modv[9])*255.9/65535-50)
    return bt1, bt2, bt3, bt4

def eng2(message):
    """Decode various Engine messages second set."""
    # global arr
    msg2 = message[0].data
    #print(msg2)
    load = ((msg2[2]*20)/51) #engine load
    Map = msg2[3] #manifold air pressure
    Iat = msg2[4]-40 #intake air temperature
    At = msg2[5]-40 #ambient temperature
    Ap = msg2[6] #atmospher pressure
    cTmp = msg2[7]-40 #cooland temperature
    rpm = ((msg2[8]*256+msg2[9])/4) #engine speed
    vsp = msg2[10]#vehicle speed
    ert = msg2[11]*256+msg2[12] #engine run time
    tp = msg2[13]*20/51 #throttle position
    ap1 = msg2[14]*20/51 #accelerator pedal position 1
    ap2 = msg2[15]*20/51 #accelerator pedal position 2
    dtcw = msg2[16]  #DTC clear warm up
    dtcd = msg2[17]*256+msg2[17] #DTC clear run distance
    dtct = msg2[18]*256+msg2[19] #DTC clear Min
    bp = ((msg2[20]*256+msg2[21])/1000) #battery voltage
    soc = msg2[22]*20/51 #state of charge.
    return load, Map, Iat, At, Ap, cTmp, rpm, vsp, ert, tp, ap1, ap2, dtcw, dtcd, dtct, bp, soc # construct a Pint Quantity

#cmd = obd.commands.RPM # select an OBD command (sensor)
ceng1 = OBDCommand("ENG1",         # name
                 "Engine Query set1",   # description
                 b"2101",        # command
                 27,              # number of return bytes
                 eng1,            # decoding function
                 ECU.ENGINE,     # (optional) ECU filter
                 True)             # (optional) enable optimizations

cbv = OBDCommand("BV",         # name
                 "12V Battery voltage",   # description
                 b"2113",        # command
                 3,              # number of return bytes
                 bvolt,            # decoding function
                 ECU.ALL,     # (optional) ECU filter
                 True,             # (optional) enable optimizations
                 header=ECU_HEADER.PCH7C0)             

cbv2 = OBDCommand("BV2",         # name
                 "12V Battery voltage",   # description
                 b"0142",        # command
                 4,              # number of return bytes
                 b2volt,            # decoding function
                 ECU.ALL,     # (optional) ECU filter
                 True)             # (optional) enable optimizations

cmv = OBDCommand("MV",         # name
                 "Module Voltages",   # description
                 b"2181",        # command
                 26,              # number of return bytes
                 modvolt,            # decoding function
                 True, # (optional) enable optimizations
                 header=ECU_HEADER.PCH700) #header       

cmesr = OBDCommand("MESR",         # name
                 "Module Internal Resistance",   # description
                 b"2195",        # command
                 12,              # number of return bytes
                 modEsr,            # decoding function
                 True, # (optional) enable optimizations
                 header=ECU_HEADER.PCH700) #header    
   
cbtemp = OBDCommand("MTMP",         # name
                 "battery temperatures",   # description
                 b"2187",        # command
                 10,              # number of return bytes
                 modTmp,            # decoding function
                 True, # (optional) enable optimizations
                 header=ECU_HEADER.PCH700) #header 

ceng2 = OBDCommand("ENG2",         # name
                 "Engine Query set 2",   # description
                 b"2101",        # command
                 24,              # number of return bytes
                 eng2,            # decoding function
                 True,           # (optional) enable optimizations
                 header=ECU_HEADER.PCH7)             

##########
#Callback functions
#these are given the responce from each decoding function. Grab data here
# will continuously print new values for each command requested
def new_ENG1(response):
    """Print responce."""
    global arr_ENG1
    try:
        arr_ENG1 = (response.value,)
    except:
        arr_ENG1 = ('NAN',)
    #print("RPM", str(arr_ENG1))
def new_BV(response):
    """Print responce."""
    global arr_BV
    try:
        arr_BV = (response.value,)
    except:
        arr_BV = ('NAN',)
    #print("12v Bat V", str(response.value))
def new_B2V(response):
    """Print responce."""
    global arr_B2V
    try:
        arr_B2V = (response.value,)
    except:
        arr_B2V = ('NAN',)
    #print("12v Bat V2", str(response.value))
def new_MV(response):
    """Print responce."""
    global arr_MV
    try:
        arr_MV = response.value
    except:
        arr_MV = ['NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN']
    #print("Module Voltages", str(response.value))
def new_MESR(response):
    """Print responce."""
    global arr_MESR
    try:
        arr_MESR = response.value
    except:
        arr_MESR = ['NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN']
    #print("Drive Bat ESRs", str(response.value))
def new_MTMP(response):
    """Print responce."""
    global arr_MTMP
    try:
        arr_MTMP = response.value
    except:
        arr_MTMP = ['NAN','NAN','NAN','NAN']
    #print("Drive Bat Temps", str(response.value))
def new_ENG2(response):
    """Print responce."""
    global arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2, writcsv, dat
    try:
        arr_ENG2 = response.value
    except:
        arr_ENG2 = ['NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN']
    dat = np.concatenate((arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2),axis =0)

    # for item in [arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2]:
    #     print (type(item))
    #     print (item)
    #print(arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2)
    writcsv.writerow(dat) #write to CSV after all row data has been collected
    dat=[]
    #print("Engine Properties", str(arr_ENG2))

#connection = obd.OBD() # auto-connects to USB or RF port
#connection = obd.Async(portstr=("/dev/rfcomm0"), baudrate=(38400), protocol=(6)) # create an asynchronous connection

#start connection while on the car
# connection = obd.Async()

#start connection while on the desktop simulated via com-o-com and python -m elm -s car on port COM4
PORT='\.\COM4'
BAUD = '38400'
BAUD = '9600'
PROTOCOL = '6'
connection = obd.Async(portstr=(PORT),baudrate=(BAUD),protocol=(PROTOCOL), fast=True)

############
#Decoding Fuctions need a filter to
#remove the unsupported messages, such as "WARNING:obd.obd:'b'2181': Module Voltages' is not supported"
connection.supported_commands.add(ceng1)
connection.supported_commands.add(cmv)
connection.supported_commands.add(cbv)
connection.supported_commands.add(cbv2)
connection.supported_commands.add(cmesr)
connection.supported_commands.add(cbtemp)
connection.supported_commands.add(ceng2)
#response = connection.query(cmd) # send single command
#print(response) # "2410 RPM"

# list of PIDs to keep refreshing
connection.watch(ceng1, callback=new_ENG1)
connection.watch(cmv, callback=new_MV)
connection.watch(cbv, callback=new_BV)
connection.watch(cbv2, callback=new_B2V)
connection.watch(cmesr, callback=new_MESR)
connection.watch(cbtemp, callback=new_MTMP)
connection.watch(ceng2, callback=new_ENG2)
#start loop
connection.start()
time.sleep(6) # keep looping for this many seconds. Do other work in the main thread
connection.stop()
#sys.stdout.close()
csvfile.close()
