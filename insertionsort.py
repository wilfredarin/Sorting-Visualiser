import pygame
import displayfiles
import visual_main
import random



screen_width,screen_height = 800,600
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
speed = 30
SizeArr = 40


arr = []
for i in range(SizeArr):
	arr.append(random.randint(10,80))

red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
white = (255,255,255)
grey = (10,118,119)

img = pygame.image.load("wall2.jpeg")


def startAgain():
	arr = []
	for i in range(SizeArr):
		arr.append(random.randint(10,80))
	insertionSort(arr)
def getOut():
	print("s")

def visualQuit():
	pygame.quit()
	quit()


def insertionSort(a):
	n = len(a)
	for i in range(1,n):
		place_key = a[i]
		#9 8 5 4
		j = i-1 
		while j>=0 and place_key<a[j]:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					closed = True
					exit()
			img = pygame.image.load("wall2.jpeg")
			screen.blit(img,[0,0])
			displayfiles.message_display("Insertion Sort",[400,50],white)
			displayfiles.displayArray(a,j)
			displayfiles.button("Complexity : O(n^2)",550,100,250,30,red,grey)
			displayfiles.button("Inplace Sort",550,150,250,30,red,grey)
			displayfiles.button("Swap Elements",550,200,250,30,red,grey)
			pygame.display.update()
			
			clock.tick(speed)
			a[j+1] = a[j]
			j-=1 
		a[j+1] = place_key 


def insertionmain():
	img = pygame.image.load("wall2.jpeg")
	screen.blit(img,[0,0])
	displayfiles.message_display("Insertion Sort",[400,50],white)
	pygame.display.update()
	
	done = True
	while done:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				done = False
		if arr!=sorted(arr):
			insertionSort(arr)
		displayfiles.button("Start",50,500,150,30,red,bright_red,startAgain)
		done = displayfiles.button("Home",450,500,150,30,red,bright_red,getOut)
		
		displayfiles.button("Quit",650,500,150,30,red,bright_red,visualQuit)


		displayfiles.button("Complexity : O(nlogn)",550,100,250,30,red,grey)
		displayfiles.button("Inplace Sort",550,150,250,30,red,grey)
		displayfiles.button("Swap Elements",550,200,250,30,red,grey)
		pygame.display.update()
	
