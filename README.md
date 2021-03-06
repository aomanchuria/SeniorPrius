# SeniorPrius
<img width="1163" alt="Screenshot 2022-01-11 204719" src="https://user-images.githubusercontent.com/27635849/149065815-a9a06107-24f4-4e81-a496-441b22dc7c8e.png">

A script to log prius data from OBD port. The image above is from libre office from the CSV file. Tested using a Bluetooth dongle in a Prius C 2014. Notice that this prius only has 10 modules. So you will have to develop something for the larger prii. But this can help you tremendously.

<img width="585" alt="image" src="https://user-images.githubusercontent.com/27635849/150472329-63a92b40-ab45-4843-81d5-ea3aa694ebe4.png">
This image is of work in progress. It shows the same read data from my commute today. A Dash Plotly server will be showing the data live as it is generated. Plotly allows one to easily navigate the data by zooming in and out as desired from the website. The site would be local, being served by the raspberry pi data logger.

First of all, here are the real heros behind this effort, on who's shoulders I am standing, without knowing anyone there:

https://github.com/brendan-w/python-OBD

https://github.com/Ircama/ELM327-emulator

Thanks guys and I hope your shoulders don't hurt. I'll add the GPL references when I release this. its an annoying thing like a reference for a 1000 word essay.

To run the script simply run this on the commandline:

```bash
python3 SeniorPrius_V0001.py
```

this will run for as many seconds as you want:
```python
time.sleep(60) # change 60 to whatever number of seconds you want, but watch out! it will literally run for that long regardless of failure
```
if it works you will see your OBD LEDS light up

I'm using a "Bafx Products - Wireless Bluetooth OBD2 Scanner & Code Reader" but if you used Dr. Prius on your phone with another reader, that should work
This script can be run on a Raspberrypi Zero. It seems to keep up just fine. Initially I was after just loging the battery voltages, but it seems that many other parts are possible. An excel file is attached, which I have added some more information to from the original. I may complete all the PIDS one day, but the really crucial steps are already done so you can get whatever you want with a little bit of modification.

This script imports and uses:
https://python-obd.readthedocs.io/en/latest/

Here is a list of imports that may be of interest
```python
import obd
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int
import time
import sys
import logging
import csv
```

this line may work to connect the blutooth... I have not tested. I bind it directly on linux:
```python
os.system("sudo rfcomm connect hci0 AA:BB:CC:11:22:33 1 &")	# connect using OBD2 unit's mac address. rfcomm locks, so detach(using "&")
```
instead I bind the bluetooth directly from linux:
https://forums.raspberrypi.com/viewtopic.php?t=125922
https://fsjohnny.medium.com/connecting-your-bluetooth-obdii-adapter-or-other-serial-port-adapters-to-a-raspberry-pi-3-f2c9663dae73

```python
sudo rfcomm bind 0 XX:XX:XX:XX:XX:XX 1
Now /dev/rfcomm0 is created and just waits there for our python script to use
```

To do this automatically at booot add these lines to RC local

```python
pi@raspberrypi:~ $ sudo nano /etc/rc.local

#connect to OBDII adapter for SeniorPrius App
#bind the address to device rfcomm 0 channel 1
rfcomm bind 0 XX:XX:XX:XX:XX:XX 1
```
then Ctrl o and Ctrl x to save and exit

a little out of order, but you need to find and trust the OBD device. This is done once.

```python
pi@raspberrypi:~ $ bluetoothctl
Agent registered
[bluetooth]#Agent on
[bluetooth]#Scan on
[bluetooth]#Scan off  ##after you found your device address
[bluetooth]#pair XX:XX:XX:XX:XX:XX ###replace with your own device address ofcourse
[bluetooth]#trust XX:XX:XX:XX:XX:XX
[bluetooth]#exit
```

Another way to setup the auto start is how I actually did it in my latest version using two services:

```python
sudo nano /lib/systemd/system/rfcomm.service

[Unit]
Description= This binds rfcomm0 to channel 1 for SeniorPrius App
After=bluetooth.service

[Service]
Type=simple
ExecStart=rfcomm bind 0 00:1D:A5:20:17:8D 1
Restart=on-failure

[Install]
WantedBy=multi-user.target


sudo nano /lib/systemd/system/SeniorPrius.service

 [Unit]
 Description=SeniorPrius App
 After=rfcomm.service

 [Service]
 Type=idle
 WorkingDirectory=/home/obd
 ExecStart=/usr/bin/python3 /home/obd/SeniorPrius_V0001.py > /home/obd/SeniorPrius.log 2>&1
 Restart=on-failure

 [Install]
 WantedBy=multi-user.target
```
After creating the services you should enable them and start them or just reboot after enabling.
```python
systemctl enable rfcomm.service
systemctl enable SeniorPrius.service

Also dont forget to make the app executable and assign 664 to the service ( its in my notes, I forget why)

chmod +x SeniorPrius_V0001.py
sudo chmod 644 /lib/systemd/system/SeniorPrius.service
sudo systemctl daemon-reload

systemctl start rfcomm.service
systemctl start SeniorPrius.service

Notice that the service will run and keep restarting regardless of what may be going on outside
so if you bring the pi home, you should stop it

systemctl stop SeniorPrius.service

```

Okay after this, every time you boot, the pi will find your bluetooth address and bind it to the serial port.

on with the python stuff...

```python
#either like this for a single command connection
connection = obd.OBD() # auto-connects to USB or RF port
#like this for an automatically updating connection with defining actually what device to use, baud rate etc (this did not work for me)
connection = obd.Async(portstr=("/dev/rfcomm0"), baudrate=(38400), protocol=(6)) # create an asynchronous connection
#or like this for automated updates with automated connection
connection = obd.Async()
```


I am also using Balena Wifi-connect: https://github.com/balena-os/wifi-connect to create a hot spot from the rpi Zero.
Basic operation:
1) plug rpi zero near your router and wait at least 2 to 5 minutes for a wifi spot to be created...annoying!
2) connect to this hotspot using your phone.
3) sign-in to your router
4) open the rpi via samba server so you can add and modify scrips or download resulting data
5) Go to your car and plug the rpi there and repeat the hot spot process, but instead of logging in to the the 3 dots on the upper rigth corner and "use connection as is"
6) Now you can use "termius" https://termius.com/ on your phone to actually run scripts on the rpi zero

Using this process you can run scripts and do small tweeks without having to go to your main computer.... Or you could just connect to your laptop... or you could leave the car running and just connect to your house router if its near by... mine is not. Termius is great if you want to continue tweeking after a good run on your car and not near your house.

hardware, this is exactly 100% all you need (plus your computer, phone, laptop, router):
https://www.amazon.com/gp/product/B009ZIILLI/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B005NLQAHS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B01GEHPI0E/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B003M0NURK/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B075CJMJYJ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B003MTTJOY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B00QTE09SY/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B01G9W1SBW/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B01NBHYAR0/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1


To test the software, instead of walking outside for every change in the 0 celcius weather, I'm using now the ELM emulator from: https://github.com/Ircama/ELM327-emulator.
Create a COM# port pair like COM3 and COM4 using comOcom (extreemely easy to use), then run the emulator like this:
python -m elm -s car  #this will pick one of the two ports, say COM3

Then use YAT to connect to COM4 and do manual commands or use Senior Prius as shown below to see it run on your computer without a car... only works if the commands are listed for your specifi car (even non hybrids) of course, but this will help you get started I think.


Using seniorPrius to connect to your car:
```python
connection = obd.Async()
```
Using SeniorPrius to connect to your COM# port

```python
PORT='\.\COM4'
BAUD = '9600' #other faster bauds are OK I think
PROTOCOL = '6'
connection = obd.Async(portstr=(PORT),baudrate=(BAUD),protocol=(PROTOCOL), fast=True)
```
