# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:00:54 2021

@author: imjprojts
This file creates a log.csv in the same folder that contains data from the OBD port
"""
#import bluetooth
import numpy as np
import os
import obd
import time
from obd import OBDCommand #, Unit
from obd.protocols import ECU
from obd.protocols import ECU_HEADER
import csv



class ElPrius:
    def __init__(self):
        #self.timestr = time.strftime("%Y%m%d-%H%M%S")
        i = 0
        while os.path.exists("output%s.csv" % i):
            i += 1
        self.timestr = "output%s" % i
        self.timestr = self.timestr + ".csv"

        self.csvfile = open(self.timestr, 'a', newline='')
        self.writcsv = csv.writer(self.csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        self.arr_ENG1=np.array(['RPM'])
        self.arr_BV=np.array(['B+'])
        self.arr_B2V=np.array(['B2+'])
        self.arr_MV=np.array(['m1v', 'm2v', 'm3v', 'm4v', 'm5v', 'm6v', 'm7v', 'm8v', 'm9v', 'm10v'])
        self.arr_MA=np.array(['Bty_Curr','Chg_ctrl', 'Dischg_ctrl', 'Delta_SOC', 'SOC_ig_on', 'SOC_max', 'SOC_min'])
        self.arr_MESR=np.array(['m1r', 'm2r', 'm3r', 'm4r', 'm5r', 'm6r', 'm7r', 'm8r', 'm9r', 'm10r'])
        self.arr_MTMP=np.array(['bt1', 'bt2', 'bt3','bt4'])
        self.arr_ENG2=np.array(['eng2Load', 'eng2Map', 'eng2Iat', 'eng2At', 'eng2Ap', 'eng2cTmp', 
                'eng2rpm', 'eng2vsp', 'eng2ert', 'eng2tp', 'eng2ap1', 'eng2ap2', 
                'eng2dtcw', 'eng2dtcd', 'eng2dtct', 'eng2bp', 'eng2soc'])
        
        dat = np.concatenate((self.arr_ENG1, self.arr_BV, self.arr_B2V, self.arr_MV, self.arr_MA, self.arr_MESR, self.arr_MTMP, self.arr_ENG2))
        
        self.writcsv.writerow(dat) #write to CSV after all row data has been collected
        dat=[]
    
  
        
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
        #define commands to give to the Prius C
        #cmd = obd.commands.RPM # select an OBD command (sensor)
        self.ceng1 = OBDCommand("ENG1",         # name
                         "Engine Query set1",   # description
                         b"2101",        # command
                         27,              # number of return bytes
                         self.eng1,            # decoding function
                         ECU.ENGINE,     # (optional) ECU filter
                         True)             # (optional) enable optimizations
        
        self.cbv = OBDCommand("BV",         # name
                         "12V Battery voltage",   # description
                         b"2113",        # command
                         3,              # number of return bytes
                         self.bvolt,            # decoding function
                         ECU.ALL,     # (optional) ECU filter
                         True,             # (optional) enable optimizations
                         header=ECU_HEADER.PCH7C0)             
        
        self.cbv2 = OBDCommand("BV2",         # name
                         "12V Battery voltage",   # description
                         b"0142",        # command
                         4,              # number of return bytes
                         self.b2volt,            # decoding function
                         ECU.ALL,     # (optional) ECU filter
                         True)             # (optional) enable optimizations
        
        self.cmv = OBDCommand("MV",         # name
                         "Module Voltages",   # description
                         b"2181",        # command
                         26,              # number of return bytes
                         self.modvolt,            # decoding function
                         True, # (optional) enable optimizations
                         header=ECU_HEADER.PCH700) #header 
         
        self.cma = OBDCommand("MA",         # name
                         "Pack Amperage",   # description
                         b"2198",        # command
                         10,              # number of return bytes
                         self.batamps,            # decoding function
                         True, # (optional) enable optimizations
                         header=ECU_HEADER.PCH700) #header      
        
        self.cmesr = OBDCommand("MESR",         # name
                         "Module Internal Resistance",   # description
                         b"2195",        # command
                         12,              # number of return bytes
                         self.modEsr,            # decoding function
                         True, # (optional) enable optimizations
                         header=ECU_HEADER.PCH700) #header    
           
        self.cbtemp = OBDCommand("MTMP",         # name
                         "battery temperatures",   # description
                         b"2187",        # command
                         10,              # number of return bytes
                         self.modTmp,            # decoding function
                         True, # (optional) enable optimizations
                         header=ECU_HEADER.PCH700) #header 
        
        self.ceng2 = OBDCommand("ENG2",         # name
                         "Engine Query set 2",   # description
                         b"2101",        # command
                         24,              # number of return bytes
                         self.eng2,            # decoding function
                         True,           # (optional) enable optimizations
                         header=ECU_HEADER.PCH7)             
        
        #########
        #Decoding Functions
        #########
    
    def eng1(self, messages):
        """Decode various Engine messages."""
        #global arr
        msg = messages[0].data
        #print(msg)
        rpm = ((msg[11]*256+msg[12])/4) 
        #arr.append(rpm)
        #print (f'Engine RPM{rpm}')
        return rpm # construct a Pint Quantity
    
    def bvolt(self, messages):
        """Decode 12v battery voltage messages."""
        #global arr
        bv = messages[0].data
        #print(bv)
        voltage = (bv[2]/10) 
        #arr.append(voltage)
        #print (f'12v Battery voltage{voltage}')
        return voltage # construct a Pint Quantity
    
    def b2volt(self, messages):
        """Decode 12v battery voltage messages."""
        #global arr
        bv = messages[0].data
        #print(bv)
        voltage = ((bv[2]*256+bv[3])/1000)  
        #arr.append(voltage)
        #print (f'12v Battery voltage{voltage}')
        return voltage # construct a Pint Quantity
    
    def modvolt(self, messages):
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
    
    def batamps(self, messages):
        """Decode pack amperage."""
        #global arr
        ba = messages[0].data
        #print(ba[2], ba[3])
        Batt_Pack_Current_Val = (ba[2] * 256 + ba[3]) / 100 - 327.68
        HV_battery_charge_control = ba[4]/2-64
        HV_battery_discharge_control = ba[5]/2-64
        Delta_SOC = ba[6]/2
        SOC_after_IG_ON = ba[7]/2
        SOC_Max = ba[8]/2
        SOC_Min = ba[9]/2
        #arr.append(voltage)
        #print (f'12v Battery voltage{voltage}')
        return Batt_Pack_Current_Val, HV_battery_charge_control, HV_battery_discharge_control, Delta_SOC, SOC_after_IG_ON, SOC_Max, SOC_Min # construct a Pint Quantity
    
    def modEsr(self, messages):
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
    
    def modTmp(self, messages):
        """Decode module temperature messages."""
        #global arr
        modv = messages[0].data
    
        bt1 = ((modv[2]*256+modv[3])*255.9/65535-50)
        bt2 = ((modv[4]*256+modv[5])*255.9/65535-50)
        bt3 = ((modv[6]*256+modv[7])*255.9/65535-50) 
        bt4 = ((modv[8]*256+modv[9])*255.9/65535-50)
        return bt1, bt2, bt3, bt4
    
    def eng2(self, message):
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
    

    
    ##########
    #Callback functions
    #these are given the responce from each decoding function. Grab data here
    # will continuously print new values for each command requested
    def new_ENG1(self, response):
        """Print responce."""
        #global arr_ENG1
        try:
            self.arr_ENG1 = (response.value,)
        except:
            self.arr_ENG1 = ('NAN',)
        #print("RPM", str(arr_ENG1))
    def new_BV(self, response):
        """Print responce."""
        #global arr_BV
        try:
            self.arr_BV = (response.value,)
        except:
            self.arr_BV = ('NAN',)
        #print("12v Bat V", str(response.value))
    def new_B2V(self, response):
        """Print responce."""
        #global arr_B2V
        try:
            self.arr_B2V = (response.value,)
        except:
            self.arr_B2V = ('NAN',)
        #print("12v Bat V2", str(response.value))
    def new_MV(self, response):
        """Print responce."""
        #global arr_MV
        try:
            self.arr_MV = response.value
        except:
            self.arr_MV = ['NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN']
        #print("Module Voltages", str(response.value))
    def new_MA(self, response):
        """Get pack current in amps."""
        #global arr_MA
        print("Pack Amperage", str(response.value))
        try:
            self.arr_MA = response.value
        except:
            self.arr_MA = ['NAN','NAN','NAN','NAN','NAN','NAN','NAN']
        #print("Pack Amperage", str(response.value))
    def new_MESR(self, response):
        """Print responce."""
        #global arr_MESR
        try:
            self.arr_MESR = response.value
        except:
            self.arr_MESR = ['NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN']
        #print("Drive Bat ESRs", str(response.value))
    def new_MTMP(self, response):
        """Print responce."""
        #global arr_MTMP
        try:
            self.arr_MTMP = response.value
        except:
            self.arr_MTMP = ['NAN','NAN','NAN','NAN']
        #print("Drive Bat Temps", str(response.value))
    def new_ENG2(self, response):
        """Print responce."""
        #global arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MA, arr_MESR, arr_MTMP, arr_ENG2, self.writcsv, dat
        try:
            self.arr_ENG2 = response.value
        except:
            self.arr_ENG2 = ['NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN','NAN']
        dat = np.concatenate((self.arr_ENG1, self.arr_BV, self.arr_B2V, self.arr_MV, self.arr_MA, self.arr_MESR, self.arr_MTMP, self.arr_ENG2),axis =0)
    
        # for item in [arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2]:
        #     print (type(item))
        #     print (item)
        #print(arr_ENG1, arr_BV, arr_B2V, arr_MV, arr_MESR, arr_MTMP, arr_ENG2)
        self.writcsv.writerow(dat) #write to CSV after all row data has been collected
        dat=[]
        #print("Engine Properties", str(arr_ENG2))
    
    def Contacto(self):
        #connection = obd.OBD() # auto-connects to USB or RF port
        #connection = obd.Async(portstr=("/dev/rfcomm0"), baudrate=(38400), protocol=(6)) # create an asynchronous connection
        
        #start connection while on the car
        connection = obd.Async()
        
        #start connection while on the desktop simulated via com-o-com and python -m elm -s car on port COM4
        #PORT='\.\COM4'
        #BAUD = '38400'
        #BAUD = '9600'
        #PROTOCOL = '6'
        #connection = obd.Async(portstr=(PORT),baudrate=(BAUD),protocol=(PROTOCOL), fast=True)
        
        ############
        #Decoding Fuctions need a filter to
        #remove the unsupported messages, such as "WARNING:obd.obd:'b'2181': Module Voltages' is not supported"
        connection.supported_commands.add(self.ceng1)
        connection.supported_commands.add(self.cmv)
        connection.supported_commands.add(self.cma)
        connection.supported_commands.add(self.cbv)
        connection.supported_commands.add(self.cbv2)
        connection.supported_commands.add(self.cmesr)
        connection.supported_commands.add(self.cbtemp)
        connection.supported_commands.add(self.ceng2)
        #response = connection.query(cmd) # send single command
        #print(response) # "2410 RPM"
        
        # list of PIDs to keep refreshing
        connection.watch(self.ceng1, callback=self.new_ENG1)
        connection.watch(self.cmv, callback=self.new_MV)
        connection.watch(self.cma, callback=self.new_MA)
        connection.watch(self.cbv, callback=self.new_BV)
        connection.watch(self.cbv2, callback=self.new_B2V)
        connection.watch(self.cmesr, callback=self.new_MESR)
        connection.watch(self.cbtemp, callback=self.new_MTMP)
        connection.watch(self.ceng2, callback=self.new_ENG2)
        
            #start loop
        connection.start()
        time.sleep(3600) # keep looping for this many seconds. Do other work in the main thread
        connection.stop()
        self.csvfile.close()

if __name__ == '__main__':
    myprius = ElPrius()
    myprius.Contacto()

