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
	mergeSort(arr)
def getOut():
	print("s")

def visualQuit():
	pygame.quit()
	quit()


def mergeSort(a):
	if len(a)>1:
		mid = len(a)//2 
		left  = a[:mid]
		right = a[mid:]
		mergeSort(left)
		mergeSort(right)
		i,j,k= 0,0,0
		while i<len(left) and j<len(right):
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					closed = True
					exit()
			screen.blit(img,[0,0])
			displayfiles.message_display("Merge Sort",[400,50],white)
			
			displayfiles.button("Quit",650,500,150,30,red,bright_red,visualQuit)
			displayfiles.button("Complexity : O(nlogn)",550,100,250,30,red,grey)
			displayfiles.button("Inplace Sort",550,150,250,30,red,grey)
			displayfiles.button("Swap Elements",550,200,250,30,red,grey)
			displayfiles.displayArray(a,k)
			pygame.display.update()
			clock.tick(speed)
			if left[i]<right[j]:
				a[k]=left[i]
				i+=1
				k+=1 
			else:
				a[k]=right[j]
				j+=1 
				k+=1
		while i<len(left):
			a[k]=left[i]
			i+=1
			k+=1
		while j<len(right):
			a[k]= right[j]
			j+=1 
			k+=1 
	return 


def mergemain():
	img = pygame.image.load("wall2.jpeg")
	screen.blit(img,[0,0])
	displayfiles.message_display("Merge Sort",[400,50],white)
	pygame.display.update()
	
	done = True
	while done:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				done = False
		if arr!=sorted(arr):
			mergeSort(arr)
		displayfiles.button("Start",50,500,150,30,red,bright_red,startAgain)
		done = displayfiles.button("Home",450,500,150,30,red,bright_red,getOut)
		
		displayfiles.button("Quit",650,500,150,30,red,bright_red,visualQuit)


		displayfiles.button("Complexity : O(nlogn)",550,100,250,30,red,grey)
		displayfiles.button("Inplace Sort",550,150,250,30,red,grey)
		displayfiles.button("Swap Elements",550,200,250,30,red,grey)
		pygame.display.update()
	
