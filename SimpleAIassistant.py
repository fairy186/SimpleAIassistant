import speech_recognition
import pyttsx3
import os
import pygame
from datetime import date, datetime

light = 0
while True:
	robot_Listen = speech_recognition.Recognizer()
	robot_speak = pyttsx3.init()
	voices = robot_speak.getProperty('voices')
	robot_speak.setProperty('voice', voices[1].id)
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		robot_Listen.adjust_for_ambient_noise(mic, duration = 1) 
		audio = robot_Listen.listen(mic)

	print("...")

	try:
		you = robot_Listen.recognize_google(audio)
	except:
		you = ""
	print("You: " + you)

	if you == "":
		robot = "I cann't hear you, try again"
	elif "hello" in you:
		robot = "Hello Huy"
	elif "time" in you:
		gio = datetime.now()
		robot = gio.strftime("%H hours %M minutes")
	elif "today" in you:
		td = date.today()
		robot = td.strftime("%B %d, %Y")
	elif "turn on" in you:
		if light == 0:
			light = 1
			robot = "the lights were on"
			pygame.init()
			screen = pygame.display.set_mode((600,600))
			running = True
			BLACK = (  0,   0,   0)
			WHITE = (255, 255, 255)
			RED = (255, 0, 0)
			i = 0
			while running:
				screen.fill(BLACK)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
				if (i < 100):
					pygame.draw.rect(screen, WHITE, (200, 300, 200, 200))
					pygame.draw.circle(screen, WHITE, (300, 300), 150)
				else:
					pygame.draw.rect(screen, (255,245,75), (200, 300, 200, 200))
					pygame.draw.circle(screen, (255,245,75), (300, 300), 150)
					pygame.draw.line(screen, RED, (300, 125), (300, 25), 4)
					pygame.draw.line(screen, RED, (475, 300), (575, 300), 4)
					pygame.draw.line(screen, RED, (125, 300), (25, 300), 4)
					pygame.draw.line(screen, RED, (175, 175), (100, 100), 4)
					pygame.draw.line(screen, RED, (475, 175), (575, 75), 4)
				i = i+1
				if (i==200):
					running = False
				pygame.time.wait(10)
				pygame.display.update()
			pygame.quit()
		else:
			robot = "can not turn on the light because it is on."
	elif "turn of" in you:
		if light == 1:
			light = 0
			pygame.init()
			screen = pygame.display.set_mode((600,600))
			running = True
			BLACK = (  0,   0,   0)
			WHITE = (255, 255, 255)
			RED = (255, 0, 0)
			i = 0
			while running:
				screen.fill(BLACK)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						running = False
				if (i > 100):
					pygame.draw.rect(screen, WHITE, (200, 300, 200, 200))
					pygame.draw.circle(screen, WHITE, (300, 300), 150)
				else:
					pygame.draw.rect(screen, (255,245,75), (200, 300, 200, 200))
					pygame.draw.circle(screen, (255,245,75), (300, 300), 150)
					pygame.draw.line(screen, RED, (300, 125), (300, 25), 4)
					pygame.draw.line(screen, RED, (475, 300), (575, 300), 4)
					pygame.draw.line(screen, RED, (125, 300), (25, 300), 4)
					pygame.draw.line(screen, RED, (175, 175), (100, 100), 4)
					pygame.draw.line(screen, RED, (475, 175), (575, 75), 4)
				i = i+1
				if (i==200):
					running = False
				pygame.time.wait(10)
				pygame.display.update()
			pygame.quit()
			robot = "the lights were off"
		else:
			robot = "can not turn off the light because it is off."
	elif "note" in you:
		robot = "opening notepad"
		print ("Robot: " + robot)
		print ("")
		robot_speak.say(robot)
		robot_speak.runAndWait()
		os.system("Notepad")
		break
	elif "game" in you:
		robot = "opening Honkai Impact 3"
		print ("Robot: " + robot)
		print ("")
		robot_speak.say(robot)
		robot_speak.runAndWait()
		os.system('D:\\"Honkai Impact 3"\\falcon_os.exe')
		break
	elif "browser" in you:
		robot = "opening Edge"
		print ("Robot: " + robot)
		print ("")
		robot_speak.say(robot)
		robot_speak.runAndWait()
		os.system('C:\\"Program Files (x86)"\\Microsoft\\Edge\\Application\\msedge.exe')
		break
	elif "music" in you:
		robot = "opening music"
		print ("Robot: " + robot)
		print ("")
		robot_speak.say(robot)
		robot_speak.runAndWait()
		os.system('D:\\HT\\Python\\Remenber Me.mp3')
		break
	elif "bye" in you:
		robot = "bye"
		print ("Robot: " + robot)
		print ("")
		robot_speak.say(robot)
		robot_speak.runAndWait()
		break
	else:
		robot = "Sorry, I don't understand, try again"
	print ("Robot: " + robot)
	print ("")
	robot_speak.say(robot)
	robot_speak.runAndWait()