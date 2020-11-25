import pygame
import random 

screen_width,screen_height = 800,600
screen = pygame.display.set_mode([screen_width, screen_height])
font_small = 35

red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
display_width,display_height = 800,600

def text_objects(text,font,color=white):
	textSurf = font.render(text,True,color)
	return textSurf,textSurf.get_rect()

def message_display(msg,place,color=(255,255,255)):
	largeText = pygame.font.Font('freesansbold.ttf',35)
	#textRect is rect that contains it
	textSurf,textRect = text_objects(msg,largeText,color)
	#center text
	textRect.center = (place[0],place[1])
	screen.blit(textSurf,textRect)
	pygame.display.update()





def button(msg,x,y,width,height,acolor,icolor,action=None):
	"""  """
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	mx,my = mouse[0],mouse[1]
	if (x+width >=mx >= x ) and (y+height >=my > y):
		pygame.draw.rect(screen,red,(x,y,width,height))
		pygame.display.update()
		if click[0]==1 and action:
			action()
			return False
	else:
		pygame.draw.rect(screen,green,(x,y,width,height))
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	
	textSurf,textRect = text_objects(msg,smallText)
	
	textRect.center = ((x+width/2),(y+height/2))
	screen.blit(textSurf,textRect)
	pygame.display.update()
	return True







def lines(lx,ly,lw,h,color):
	pygame.draw.rect(screen,color,[lx,ly,lw,h])

def displayArray(a,j=0):
	for i in range(len(a)):
		if i==j:
			lines(100+i*2,50,2,a[i]*5,(255,0,0))
		elif i%2==0:
			lines(100+i*2,50,2,a[i]*5,(0,55,244))
		else:
			lines(100+i*2,50,2,a[i]*5,(0,255,0))
	pygame.display.update()
