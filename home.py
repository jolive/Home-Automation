import sys, pygame
import subprocess
import RPi.GPIO as GPIO
import time

#pin layout
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

img = pygame.image.load('home_1.jpg')
img2= pygame.image.load('home_2.jpg')
blueprintRED = pygame.image.load('blueprint_secure.jpg')
blueprintGREEN = pygame.image.load('blueprint_secure1.jpg')

img = pygame.transform.scale(img, (320,240))
img2 = pygame.transform.scale(img2, (320,240))
blueprintRED = pygame.transform.scale(blueprintRED, (320,240))
blueprintGREEN = pygame.transform.scale(blueprintGREEN, (320,240))

RED = (255,0,0)
GREEN = (0,153,0)

colorPower = RED
colorWater = RED
colorLocks = RED
colorSecure = RED

varPower = 0
varWater = 0
varLocks = 0
varSecure = 0

timer = 0

pygame.init()
myfont= pygame.font.SysFont("monospace", 25)
myfont2= pygame.font.SysFont("monospace", 15)
myfont3 =pygame.font.SysFont("monospace", 15)
#height and width of the sreen
#size = [640, 480]
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(960,540))
backgroundRect = background.get_rect()
size =(width, height) = background.get_size()
screen = pygame.display.set_mode(size)

#Set the title of the screen
pygame.display.set_caption("Home Automation")

#Loop until the user clocks the close button
done = False

#rendering text
label = myfont.render("Welcome Home", 1, (255, 255, 255))
label2 = myfont2.render("Home Automation", 1, (255, 255, 255))
Power = myfont3.render("Power", 1, (255, 255, 255))
Water = myfont3.render("Water", 1, (255, 255, 255))
Locks = myfont3.render("Locks", 1, (255, 255, 255))
Security = myfont.render("Home Security :", 1, (255,255,255))
Good = myfont.render("Secure", 1, (0,153,0))
Bad = myfont.render("Not Secure", 1, (255,0,0))
screen.blit(label, (10,10))

#Used to manage refresh rate
clock = pygame.time.Clock()

WHITE = (250,250,250)
#Button declaration
pygame.draw.rect(screen,WHITE,[10,50,10,10])

#Main Loop
while done == False:
    screen.blit(background, backgroundRect)
    screen.blit(label, (10,10))
    screen.blit(label2, (10,30))
    screen.blit(Security, (325,10))
    #if locks are locked and door closed
   

    pygame.draw.rect(screen,colorPower,[85,78,10,10])
    screen.blit(Power, (35,75))

    pygame.draw.rect(screen,colorWater,[155,78,10,10])
    screen.blit(Water, (105,75))

    pygame.draw.rect(screen,colorLocks,[225,78,10,10])
    screen.blit(Locks, (175,75))

    screen.blit(img,(35,125))
    

    img = pygame.image.load('home_1.jpg')

    

    for event in pygame.event.get():
	if event.type == pygame.QUIT:
		done = True
	elif event.type == pygame.MOUSEBUTTONDOWN:
		pos = pygame.mouse.get_pos()
		column = pos[0]
		row = pos[1]
		var = 0
		var1 = 0
		for var in range(10):
			column = column + 1
			if column == 95:
				for var1 in range(10):
					row = row + 1
					if row == 90:
						if varPower == 1:	
							varPower = 0
						elif varPower == 0:
							varPower = 1
							#GPIO.output(21, GPIO.HIGH)
			elif column == 165:
				for var1 in range(10):
					row = row + 1
					if row == 90:
						if varWater == 1:	
							varWater = 0
							#GPIO.output(21, GPIO.LOW)
						elif varWater == 0:
							varWater = 1
							#GPIO.output(21, GPIO.HIGH)
			elif column == 235:
				for var1 in range(10):
					row = row + 1
					if row == 90:
						if varLocks == 1:	
							varLocks = 0
							#GPIO.output(21, GPIO.LOW)
						elif varLocks == 0:
							varLocks = 1
							#GPIO.output(21, GPIO.		
		
    #update colors of boxes
    if varPower == 1:
	colorPower = GREEN
        GPIO.output(5, 1)
    elif varPower == 0:
	colorPower = RED
        GPIO.output(5, 0)

    if varWater == 1:
	colorWater = GREEN
        GPIO.output(6, 1)
    elif varWater == 0:
	colorWater = RED
        GPIO.output(6, 0)

    if varLocks == 1:
	colorLocks = GREEN
	screen.blit(blueprintGREEN,(400,125))
        GPIO.output(19, 0)
    elif varLocks == 0:
	colorLocks = RED
	screen.blit(blueprintRED,(400,125))
	GPIO.output(19, 1)
	
    if varPower == 0:
	if varWater == 0: 
		if varLocks == 1:
			screen.blit(Good, (550,10))
  			#if locks are locked and door open
		elif varLocks == 0:
   			screen.blit(Bad, (550,10))
	elif varLocks == 0:
   		screen.blit(Bad, (550,10))
    elif varLocks == 0:
   	screen.blit(Bad, (550,10))


    # Limit to 60 frames per second
    clock.tick(60)

    timer = timer + 1
    if timer == 60:
	subprocess.call("python camera2.py 1", shell=True)
	print(timer)
	timer = 0

 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

GPIO.cleanup()
pygame.quit()



