import RPi.GPIO as gpio
import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
import time
import picamera
import datetime
import os
pir=17

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(pir, gpio.IN)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))

    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))

    elif command == '/photo':
		data1= time.strftime("%d_%b_%Y|%H:%M:%S")
		with picamera.PiCamera() as camera:
        		camera.resolution = (800, 600)
        		camera.rotation = 180
			camera.start_preview()
			time.sleep(2)
			print data1
			camera.capture('%s.jpg'%data1)
			camera.stop_preview()
			time.sleep(1)
			dat='%s.jpg'%data1
			print dat
			bot.sendPhoto(chat_id=chat_id, photo=open(dat, 'rb'))


    elif command == '/siren':
	os.system("sudo omxplayer Siren.mp3")
     	bot.sendMessage(chat_id, 'Status: Siren Activated')

    elif command == '/door_open':
        os.system("sudo python dooropen.py")
        bot.sendMessage(chat_id, 'Status: Door Open')

    elif command == '/door_close':
        os.system("sudo python doorclose.py")
        bot.sendMessage(chat_id, 'Status: Door Closed')

	elif command == '/lamp1_on':
		os.system("sudo python lamp1_on.py")
		bot.sendMessage(chat_id, 'Status: LAMP1 ON')

	elif command == '/lamp1_off':
        os.system("sudo python lamp1_off.py")
        bot.sendMessage(chat_id, 'Status: LAMP1 OFF')

	elif command == '/lamp2_on':
		os.system("sudo python lamp2_on.py")
		bot.sendMessage(chat_id, 'Status: LAMP2 ON')

	elif command == '/lamp2_off':
        os.system("sudo python lamp2_off.py")
        bot.sendMessage(chat_id, 'Status: LAMP2 OFF')


    while command == '/security':
		print "Ready for sensor"
		bot.sendMessage(chat_id, 'Status: Security system activated, Alert will be sent on visitor arrival')
    		while 1:
			if gpio.input(pir)==0:

				print 'Motion detected'
				data1= time.strftime("%d_%b_%Y|%H:%M:%S")
				with picamera.PiCamera() as camera:
        				camera.resolution = (800, 600)
        				camera.rotation = 180
					camera.start_preview()
					time.sleep(2)
					print data1
					camera.capture('%s.jpg'%data1)
					camera.stop_preview()
					time.sleep(1)
					dat='%s.jpg'%data1
					print dat
					bot.sendPhoto(chat_id=chat_id, photo=open(dat, 'rb'))
				time.sleep(2)
				print'test'

				#if command == '/stop':
					#print'stop rxd'
        				#bot.sendMessage(chat_id, 'security stoped')
				return


    while command == '/stop_security':
        bot.sendMessage(chat_id, 'Security system stoped')



bot = telepot.Bot('974934601:AAH2LhhwXcxTwHk67CDMX27L3U_26oCBGDo')

MessageLoop(bot, handle).run_as_thread()
print 'I am listening ...'

while 1:
    time.sleep(10)
