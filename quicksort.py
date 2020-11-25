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
	quickSort(arr)
def getOut():
	print("s")

def visualQuit():
	pygame.quit()
	quit()


def quickSort(a):
	def partion(a,low,high):
		i = low-1
		pivot = a[high]
		for j in range(low,high):
			if a[j]<pivot:
				i+=1 
				a[i],a[j] = a[j],a[i]

				for event in pygame.event.get():
					if event.type==pygame.QUIT:
						closed = True
						exit()
			screen.blit(img,[0,0])
			displayfiles.message_display("Inseertion Sort",[400,50],white)
			displayfiles.displayArray(a,j)
			displayfiles.button("Complexity : O(nlogn)",550,100,250,30,red,grey)
			displayfiles.button("Inplace Sort",550,150,250,30,red,grey)
			displayfiles.button("Swap Elements",550,200,250,30,red,grey)
		
			pygame.display.update()
			clock.tick(speed)
		a[i+1],a[high] = a[high],a[i+1]
		return i+1 
	def quickHelp(a,low,high):
		if low<high:
			pi = partion(a,low,high)
			quickHelp(a,low,pi-1)
			quickHelp(a,pi+1,high)
	quickHelp(a,0,len(a)-1) 








def quickmain():
	img = pygame.image.load("wall2.jpeg")
	screen.blit(img,[0,0])
	displayfiles.message_display("Quick Sort",[400,50],white)
	pygame.display.update()
	
	done = True
	while done:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				done = False
		if arr!=sorted(arr):
			quickSort(arr)
		displayfiles.button("Start",50,500,150,30,red,bright_red,startAgain)
		done = displayfiles.button("Home",450,500,150,30,red,bright_red,getOut)
		
		displayfiles.button("Quit",650,500,150,30,red,bright_red,visualQuit)


		displayfiles.button("Complexity : O(nlogn)",550,100,250,30,red,grey)
		displayfiles.button("Inplace Sort",550,150,250,30,red,grey)
		displayfiles.button("Swap Elements",550,200,250,30,red,grey)
		pygame.display.update()
	
