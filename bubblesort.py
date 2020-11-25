import pygame
import displayfiles
import visual_main
import random

SizeArr = 40


arr = []
for i in range(SizeArr):
	arr.append(random.randint(10,80))




screen_width,screen_height = 800,600
screen = pygame.display.set_mode([screen_width, screen_height])


red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
speed = 30



def getOut():
	print("s")

def visualQuit():
	pygame.quit()
	quit()

def bubleSort(a):
	for i in range(len(a)):
		for j in range(len(a)-i-1):
			if a[j]>a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					closed = True
					exit()
			img = pygame.image.load("wall2.jpeg")
			screen.blit(img,[0,0])
			displayfiles.message_display("Bubble Sort",[400,50],white)
			displayArray(a,j)
			pygame.display.update()
			clock.tick(speed)

def bubblemain():
	img = pygame.image.load("wall2.jpeg")
	screen.blit(img,[0,0])
	displayfiles.message_display("Bubble Sort",[400,50],white)
	pygame.display.update()
	print("Bubble")
	done = True
	flag = False
	while done:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				done = False
		
		done = displayfiles.button("Home",450,500,150,30,red,bright_red,getOut)
		
		displayfiles.button("Quit",650,500,150,30,red,bright_red,visualQuit)

		if not flag:
			for i in range(len(arr)):
				swap = False
				for j in range(len(arr)-i-1):
					if arr[j]>arr[j+1]:
						arr[j],arr[j+1] = arr[j+1],arr[j]
						swap = True
					for event in pygame.event.get():
						if event.type==pygame.QUIT:
							closed = True
							exit()

					img = pygame.image.load("wall2.jpeg")
					screen.blit(img,[0,0])
					displayfiles.message_display("Bubble Sort",[400,50],white)
					displayfiles.displayArray(arr,j)
					pygame.display.update()
					clock.tick(speed)
				if not swap:
					flag = True
					break
		

		displayfiles.button("Time Complexity : O(n^2)",550,100,250,30,red,bright_red)
		displayfiles.button("Inplace Sort",550,150,250,30,red,bright_red)
		displayfiles.button("Swap Elements",550,200,250,30,red,bright_red)
		pygame.display.update()
	print('out of buubke')
