# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 09:00:54 2021

@author: imjprojts
"""
#import bluetooth
import obd

from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
import time



#this script will reveal the size of each command responce in bytes in the errors returned

#connection = obd.Async() # create an asynchronous connection
connection = obd.OBD() 

#os.system('sudo rfcomm connect hci1 00:1D:A5:20:17:AD 1')

#time.sleep(5)
obd.logger.setLevel(obd.logging.DEBUG)
log = open("output.txt", "a")  # append mode



def decode(messages):
    """ decoder dummy """
    d = messages[0].data
    hex = messages[0].hex()
    log.write(str(d) + '\n')
    log.write(str(hex) + '\n')
    print(str(d))
    print(str(hex))
    return d # construct a Pint Quantity



cmd0700 = OBDCommand("cmd0700","cmd0700",b"210", 2, decode, True, "700")
cmd17 = OBDCommand("cmd17","cmd17",b"2101", 2, decode, True, "7")
cmd2700 = OBDCommand("cmd2700","cmd2700",b"2101", 2, decode, True, "700")
cmd37B0 = OBDCommand("cmd37B0","cmd37B0",b"2103", 2, decode, True, "7B0")
cmd47 = OBDCommand("cmd47","cmd47",b"2103", 2, decode, True, "7")
cmd57 = OBDCommand("cmd57","cmd57",b"2104", 2, decode, True, "7")
cmd67B0 = OBDCommand("cmd67B0","cmd67B0",b"2105", 2, decode, True, "7B0")
cmd77 = OBDCommand("cmd77","cmd77",b"2105", 2, decode, True, "7")
cmd87B0 = OBDCommand("cmd87B0","cmd87B0",b"2106", 2, decode, True, "7B0")
cmd97 = OBDCommand("cmd97","cmd97",b"2106", 2, decode, True, "7")
cmd107B0 = OBDCommand("cmd107B0","cmd107B0",b"2107", 2, decode, True, "7B0")
cmd117C0 = OBDCommand("cmd117C0","cmd117C0",b"2112", 2, decode, True, "7C0")
cmd127C0 = OBDCommand("cmd127C0","cmd127C0",b"2113", 2, decode, True, "7C0")
cmd137B0 = OBDCommand("cmd137B0","cmd137B0",b"2121", 2, decode, True, "7B0")
cmd147C0 = OBDCommand("cmd147C0","cmd147C0",b"2121", 2, decode, True, "7C0")
cmd157C4 = OBDCommand("cmd157C4","cmd157C4",b"2121", 2, decode, True, "7C4")
cmd16700 = OBDCommand("cmd16700","cmd16700",b"2121", 2, decode, True, "700")
cmd177C4 = OBDCommand("cmd177C4","cmd177C4",b"2122", 2, decode, True, "7C4")
cmd187C0 = OBDCommand("cmd187C0","cmd187C0",b"2123", 2, decode, True, "7C0")
cmd197C4 = OBDCommand("cmd197C4","cmd197C4",b"2124", 2, decode, True, "7C4")
cmd207 = OBDCommand("cmd207","cmd207",b"2124", 2, decode, True, "7")
cmd217C4 = OBDCommand("cmd217C4","cmd217C4",b"2126", 2, decode, True, "7C4")
cmd227C0 = OBDCommand("cmd227C0","cmd227C0",b"2129", 2, decode, True, "7C0")
cmd237C4 = OBDCommand("cmd237C4","cmd237C4",b"2129", 2, decode, True, "7C4")
cmd247 = OBDCommand("cmd247","cmd247",b"2137", 2, decode, True, "7")
cmd257C4 = OBDCommand("cmd257C4","cmd257C4",b"2141", 2, decode, True, "7C4")
cmd26700 = OBDCommand("cmd26700","cmd26700",b"2141", 2, decode, True, "700")
cmd277B0 = OBDCommand("cmd277B0","cmd277B0",b"2142", 2, decode, True, "7B0")
cmd287C4 = OBDCommand("cmd287C4","cmd287C4",b"2143", 2, decode, True, "7C4")
cmd297C4 = OBDCommand("cmd297C4","cmd297C4",b"2144", 2, decode, True, "7C4")
cmd307B0 = OBDCommand("cmd307B0","cmd307B0",b"2146", 2, decode, True, "7B0")
cmd317B0 = OBDCommand("cmd317B0","cmd317B0",b"2147", 2, decode, True, "7B0")
cmd327 = OBDCommand("cmd327","cmd327",b"2147", 2, decode, True, "7")
cmd337B0 = OBDCommand("cmd337B0","cmd337B0",b"2148", 2, decode, True, "7B0")
cmd347C4 = OBDCommand("cmd347C4","cmd347C4",b"2149", 2, decode, True, "7C4")
cmd357 = OBDCommand("cmd357","cmd357",b"2149", 2, decode, True, "7")
cmd367C4 = OBDCommand("cmd367C4","cmd367C4",b"2153", 2, decode, True, "7C4")
cmd377B0 = OBDCommand("cmd377B0","cmd377B0",b"2158", 2, decode, True, "7B0")
cmd38700 = OBDCommand("cmd38700","cmd38700",b"2161", 2, decode, True, "700")
cmd39700 = OBDCommand("cmd39700","cmd39700",b"2162", 2, decode, True, "700")
cmd40700 = OBDCommand("cmd40700","cmd40700",b"2167", 2, decode, True, "700")
cmd41700 = OBDCommand("cmd41700","cmd41700",b"2168", 2, decode, True, "700")
cmd42700 = OBDCommand("cmd42700","cmd42700",b"2170", 2, decode, True, "700")
cmd43700 = OBDCommand("cmd43700","cmd43700",b"2171", 2, decode, True, "700")
cmd44700 = OBDCommand("cmd44700","cmd44700",b"2174", 2, decode, True, "700")
cmd45700 = OBDCommand("cmd45700","cmd45700",b"2175", 2, decode, True, "700")
cmd46700 = OBDCommand("cmd46700","cmd46700",b"2178", 2, decode, True, "700")
cmd47700 = OBDCommand("cmd47700","cmd47700",b"2179", 2, decode, True, "700")
cmd48700 = OBDCommand("cmd48700","cmd48700",b"2181", 2, decode, True, "700")
cmd49700 = OBDCommand("cmd49700","cmd49700",b"2187", 2, decode, True, "700")
cmd50700 = OBDCommand("cmd50700","cmd50700",b"2192", 2, decode, True, "700")
cmd51700 = OBDCommand("cmd51700","cmd51700",b"2195", 2, decode, True, "700")
cmd52700 = OBDCommand("cmd52700","cmd52700",b"2198", 2, decode, True, "700")
cmd53700 = OBDCommand("cmd53700","cmd53700",b"015B", 2, decode, True, "700")
cmd547B0 = OBDCommand("cmd547B0","cmd547B0",b"211D", 2, decode, True, "7B0")
cmd557B0 = OBDCommand("cmd557B0","cmd557B0",b"211F", 2, decode, True, "7B0")
cmd567B0 = OBDCommand("cmd567B0","cmd567B0",b"213C", 2, decode, True, "7B0")
cmd577C4 = OBDCommand("cmd577C4","cmd577C4",b"213C", 2, decode, True, "7C4")
cmd587 = OBDCommand("cmd587","cmd587",b"213C", 2, decode, True, "7")
cmd597B0 = OBDCommand("cmd597B0","cmd597B0",b"213D", 2, decode, True, "7B0")
cmd607C4 = OBDCommand("cmd607C4","cmd607C4",b"213D", 2, decode, True, "7C4")
cmd617C4 = OBDCommand("cmd617C4","cmd617C4",b"214A", 2, decode, True, "7C4")
cmd627C4 = OBDCommand("cmd627C4","cmd627C4",b"214B", 2, decode, True, "7C4")
cmd637C4 = OBDCommand("cmd637C4","cmd637C4",b"214C", 2, decode, True, "7C4")
cmd647B0 = OBDCommand("cmd647B0","cmd647B0",b"215A", 2, decode, True, "7B0")
cmd657B0 = OBDCommand("cmd657B0","cmd657B0",b"215F", 2, decode, True, "7B0")
cmd66700 = OBDCommand("cmd66700","cmd66700",b"217C", 2, decode, True, "700")
cmd67700 = OBDCommand("cmd67700","cmd67700",b"217D", 2, decode, True, "700")
cmd68700 = OBDCommand("cmd68700","cmd68700",b"218A", 2, decode, True, "700")
cmd69700 = OBDCommand("cmd69700","cmd69700",b"218E", 2, decode, True, "700")
cmd70700 = OBDCommand("cmd70700","cmd70700",b"219B", 2, decode, True, "700")
cmd717B0 = OBDCommand("cmd717B0","cmd717B0",b"21A1", 2, decode, True, "7B0")
cmd727C0 = OBDCommand("cmd727C0","cmd727C0",b"21A1", 2, decode, True, "7C0")
cmd737B0 = OBDCommand("cmd737B0","cmd737B0",b"21A3", 2, decode, True, "7B0")
cmd747B0 = OBDCommand("cmd747B0","cmd747B0",b"21A6", 2, decode, True, "7B0")
cmd757C0 = OBDCommand("cmd757C0","cmd757C0",b"21A7", 2, decode, True, "7C0")
cmd767B0 = OBDCommand("cmd767B0","cmd767B0",b"21BE", 2, decode, True, "7B0")
cmd777 = OBDCommand("cmd777","cmd777",b"21C1", 2, decode, True, "7")
cmd78700 = OBDCommand("cmd78700","cmd78700",b"21C1", 2, decode, True, "700")
cmd79700 = OBDCommand("cmd79700","cmd79700",b"21C2", 2, decode, True, "700")
connection.supported_commands.add(cmd0700)
connection.supported_commands.add(cmd17)
connection.supported_commands.add(cmd2700)
connection.supported_commands.add(cmd37B0)
connection.supported_commands.add(cmd47)
connection.supported_commands.add(cmd57)
connection.supported_commands.add(cmd67B0)
connection.supported_commands.add(cmd77)
connection.supported_commands.add(cmd87B0)
connection.supported_commands.add(cmd97)
connection.supported_commands.add(cmd107B0)
connection.supported_commands.add(cmd117C0)
connection.supported_commands.add(cmd127C0)
connection.supported_commands.add(cmd137B0)
connection.supported_commands.add(cmd147C0)
connection.supported_commands.add(cmd157C4)
connection.supported_commands.add(cmd16700)
connection.supported_commands.add(cmd177C4)
connection.supported_commands.add(cmd187C0)
connection.supported_commands.add(cmd197C4)
connection.supported_commands.add(cmd207)
connection.supported_commands.add(cmd217C4)
connection.supported_commands.add(cmd227C0)
connection.supported_commands.add(cmd237C4)
connection.supported_commands.add(cmd247)
connection.supported_commands.add(cmd257C4)
connection.supported_commands.add(cmd26700)
connection.supported_commands.add(cmd277B0)
connection.supported_commands.add(cmd287C4)
connection.supported_commands.add(cmd297C4)
connection.supported_commands.add(cmd307B0)
connection.supported_commands.add(cmd317B0)
connection.supported_commands.add(cmd327)
connection.supported_commands.add(cmd337B0)
connection.supported_commands.add(cmd347C4)
connection.supported_commands.add(cmd357)
connection.supported_commands.add(cmd367C4)
connection.supported_commands.add(cmd377B0)
connection.supported_commands.add(cmd38700)
connection.supported_commands.add(cmd39700)
connection.supported_commands.add(cmd40700)
connection.supported_commands.add(cmd41700)
connection.supported_commands.add(cmd42700)
connection.supported_commands.add(cmd43700)
connection.supported_commands.add(cmd44700)
connection.supported_commands.add(cmd45700)
connection.supported_commands.add(cmd46700)
connection.supported_commands.add(cmd47700)
connection.supported_commands.add(cmd48700)
connection.supported_commands.add(cmd49700)
connection.supported_commands.add(cmd50700)
connection.supported_commands.add(cmd51700)
connection.supported_commands.add(cmd52700)
connection.supported_commands.add(cmd53700)
connection.supported_commands.add(cmd547B0)
connection.supported_commands.add(cmd557B0)
connection.supported_commands.add(cmd567B0)
connection.supported_commands.add(cmd577C4)
connection.supported_commands.add(cmd587)
connection.supported_commands.add(cmd597B0)
connection.supported_commands.add(cmd607C4)
connection.supported_commands.add(cmd617C4)
connection.supported_commands.add(cmd627C4)
connection.supported_commands.add(cmd637C4)
connection.supported_commands.add(cmd647B0)
connection.supported_commands.add(cmd657B0)
connection.supported_commands.add(cmd66700)
connection.supported_commands.add(cmd67700)
connection.supported_commands.add(cmd68700)
connection.supported_commands.add(cmd69700)
connection.supported_commands.add(cmd70700)
connection.supported_commands.add(cmd717B0)
connection.supported_commands.add(cmd727C0)
connection.supported_commands.add(cmd737B0)
connection.supported_commands.add(cmd747B0)
connection.supported_commands.add(cmd757C0)
connection.supported_commands.add(cmd767B0)
connection.supported_commands.add(cmd777)
connection.supported_commands.add(cmd78700)
connection.supported_commands.add(cmd79700)
response = connection.query(cmd0700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd17) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd2700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd37B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd47) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd57) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd67B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd77) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd87B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd97) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd107B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd117C0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd127C0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd137B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd147C0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd157C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd16700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd177C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd187C0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd197C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd207) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd217C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd227C0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd237C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd247) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd257C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd26700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd277B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd287C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd297C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd307B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd317B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd327) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd337B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd347C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd357) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd367C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd377B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd38700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd39700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd40700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd41700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd42700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd43700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd44700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd45700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd46700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd47700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd48700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd49700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd50700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd51700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd52700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd53700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd547B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd557B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd567B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd577C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd587) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd597B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd607C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd617C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd627C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd637C4) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd647B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd657B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd66700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd67700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd68700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd69700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd70700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd717B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd727C0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd737B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd747B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd757C0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd767B0) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd777) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd78700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1) 
response = connection.query(cmd79700) # send the command
log.write(str(response.value) + '\n')
print(str(response.value) + '\n')
time.sleep(1)   

#connection.start()
#time.sleep(5) # do other work in the main thread
#connection.stop()
connection.close()