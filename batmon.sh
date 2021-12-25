#!/bin/bash
#this script waits for 60 seconds, then starts the SeniorPrius script
#use this as a cron job at boot time
/bin/sleep 60 && /usr/bin/python3 /home/pi/Documents/SeniorPrius_V0001.py
