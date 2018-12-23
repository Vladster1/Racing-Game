import pygame
import time
import random 

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 200, 0)

car_width = 90

gameDisplay = pygame.display.set_mode((display_width,display_height)) #resolution
pygame.display.set_caption("A Racing Game!") #Title of window
clock = pygame.time.Clock() #FPS

bikeImg = pygame.image.load("Car.png") #imports car image
bikeImg = pygame.transform.scale(bikeImg, (90,120)) #makes it smaller

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged " +str(count), True, black) #True means AA
	gameDisplay.blit(text,(0,0))
	
def things(thingx, thingy, thingw, thingh, color): #obstacles
	pygame.draw.rect(gameDisplay, red, [thingx, thingy, thingw, thingh])


def bike(x,y):
	gameDisplay.blit(bikeImg,(x,y)) #displays car
																		
def text_objects(text, font):											
	textSurface = font.render(text, True, black) #text, AA, color
	return textSurface, textSurface.get_rect()	

def message_display(text):
	largeText = pygame.font.Font("freesansbold.ttf",115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	
	pygame.display.update()
	
	time.sleep(2)
	
	game_loop()

def crash():
	message_display("You Crashed!")
	
def button(msg,x,y,w,h,ic,ac,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	print(click)
	
		
	if x + w > mouse[0] > x and y + 50 > mouse[1] > y:
		pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
		if click[0] == 1 and action!= None:
			if action == "play":
				game_loop()
	else:
		pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
		
	smallText = pygame.font.Font("freesansbold.ttf", 20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)
	
def game_intro():
	intro = True
	
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		gameDisplay.fill(white)
		largeText = pygame.font.Font("freesansbold.ttf", 100)
		TextSurf, TextRect = text_objects("A Racing Game", largeText)
		TextRect.center = ((display_width/2), (display_height/2))
		gameDisplay.blit(TextSurf, TextRect)
		
		button("Go!",350,450,100,50,green,dark_green,"play")
		
		pygame.display.update()
		clock.tick(15)
		
def game_loop():
	x = (display_width * 0.45) #centers
	y = (display_height * 0.8)

	x_change = 0

	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 8
	thing_width = 100
	thing_height = 100
	
	dodged = 0
	
	gameExit = False #crashed false allows program to run

	while not gameExit:
		
		for event in pygame.event.get(): #allows us to leave
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN: #keycontrol
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
								
		x += x_change #updates constantly
				
		
		gameDisplay.fill(white) #background
		
		
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed
		bike(x,y)
		things_dodged(dodged)
		
		if x > display_width - car_width or x < 0:
			crash()
		
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 1
			thing_width += (dodged * 1.2)
			
		if y < thing_starty+thing_height:
			print("y crossover")
			
			if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
				print("x crossover")
				crash()
		
		
		
			
		pygame.display.update()
		clock.tick(60)

game_intro() 
		
game_loop()
	
pygame.quit()
quit()
		

