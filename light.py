#!/usr/bin/python

#############################
## NB: before using this   ##
## make sure AppleScript   ##
## for python is installed ##
#############################

# arrow key codes:
# LEFT: (key code 123)
# RIGHT: key code 124)
# UP: (key code 126)
# DOWN: (key code 125)

import os
from time import sleep
from applescript import AppleScript as aps
def apcmd(cmd,delay=0.3,times=1):
	""" executes AppleScript command
		Args:
			cmd (str): command to execute
			delay(float,optional): how long to wait after command executes (in seconds). default: 0.3
			times(int,optional): how many times to execute the comand. default: 1
		Returns:
			result of the applescript command
	"""
	result = False
	try:
		for i in xrange(times):
			result = aps(cmd).run()
			sleep(delay)
		return result
	except Exception, e:
		print "CMD FAILED!!!",cmd, 'x',str(times)
		# raise e

# from apcmd import apcmd
# waits for a window that contains specified name in the specified process
def waitWindow(name,process="Photomatix Pro"):
	while(len(apcmd('tell application "System Events" to tell application process "'+process+'" to return windows whose name contains "'+name+'"',delay=1))<1):
		pass
# apcmd('tell application "Photomatix Pro" to activate')
# print apcmd('tell application "System Events" to tell application process "Photomatix Pro" to return name of every window')

stopsToAdjust = 2

# bring LR to the front
apcmd('tell application "Lightroom" to activate')
# create 2 virtual copies
apcmd('tell application "System Events" to keystroke "\'" using command down',times=2)
# go into develop mode
apcmd('tell application "System Events" to keystroke "d"')
# decrease exposure defined number of stops
apcmd('tell application "System Events" to keystroke "-"',delay=0.05,times=stopsToAdjust*10)
sleep(0.5)
# go to previous photo
apcmd('tell application "System Events" to key code 123')
# increase exposure defined number of stops
apcmd('tell application "System Events" to keystroke "+"',delay=0.05,times=stopsToAdjust*10)
sleep(0.5)
# go back to Library
apcmd('tell application "System Events" to keystroke "g"')
# go to the first image
apcmd('tell application "System Events" to key code 123')
# select all 3 images
apcmd('tell application "System Events" to key code 124 using shift down',times=2)

# open Export to Photomatix dialog
apcmd('tell application "System Events" to tell process "Lightroom" to tell menu bar 1 to tell menu bar item "File" to tell menu "File" to tell menu item "Export with Preset" to tell menu "Export with Preset" to click menu item "Photomatix Pro"')
# add 'hdr' to the end of the file name
apcmd('tell application "System Events" to key code 48 using shift down',times=4) #tab
apcmd('tell application "System Events" to key code 124')
apcmd('tell application "System Events" to keystroke (ASCII character 8)') #backspace
apcmd('tell application "System Events" to keystroke "hdr"')
# open photomatix
apcmd('tell application "System Events" to keystroke return')
# wait until Photomatix opens
while (os.system("ps ax | grep Photomatix | grep -v xClient | grep -v grep > /dev/null")):
	sleep(1)
apcmd('tell application "Photomatix Pro" to activate')

# wait until Exposure settings window shows up
waitWindow('Exposure')

# set exposure to the defined number of stops
apcmd('tell application "System Events" to key code 126')
apcmd('tell application "System Events" to keystroke "'+str(stopsToAdjust)+'"')
apcmd('tell application "System Events" to keystroke return',times=2)

# wait until window Adjustments shows up
waitWindow('Adjustments')

## --- automate photomatix --- ##
# TO BE ABLE TO MAKE ADJUSTMENTS IN PHOTOMATIX PRO, COMMENT OUT THIS BLOCK 

# hit enter in that window (to save and re-import)
apcmd('''
	tell application "System Events" 
		tell application process "Photomatix Pro" 
			set frontmost to true
			perform action "AXRaise" of (windows whose title contains "Adjustments")
		end tell
	end tell
''')
apcmd('tell application "System Events" to keystroke return')

## --- end automate photomatix --- ##

# wait until the save window disappears
while (len(apcmd('tell application "System Events" to tell application process "Photomatix Pro" to return name of every window',delay=1))>1):
	pass

#wait until the Photomatix app is closed
# while (not os.system("ps ax | grep Photomatix | grep -v xClient | grep -v grep > /dev/null")):
# 	sleep(1)

apcmd('tell application "Lightroom" to activate')
# clear selection
apcmd('tell application "System Events" to key code 124')
# select 2 virtual copies
apcmd('tell application "System Events" to key code 123')
apcmd('tell application "System Events" to key code 123 using shift down')
# mark them as rejected
apcmd('tell application "System Events" to keystroke "x"')
# mark the original as pick (to hide it)
apcmd('tell application "System Events" to key code 123')
apcmd('tell application "System Events" to keystroke "p"')
