import pygame 
import displayfiles
import bubblesort
import insertionsort
import mergesort
import quicksort


pygame.init()

red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
white = (255,255,255)



screen_width,screen_height = 800,600
screen = pygame.display.set_mode([screen_width, screen_height])









def visualQuit():
	pygame.quit()
	quit()


def mainVisual():
	
	
	close = True
	while close:
		mouse = pygame.mouse.get_pos()
		#print(mouse)
		
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				close = False
		img = pygame.image.load("wall.jpg")
		screen.blit(img,[0,0])
		pygame.display.update()
		displayfiles.message_display("Welcome To Sort Visualizer",[400,100],white)
		
		displayfiles.button("Bubble Sort",400,300,150,30,red,bright_red,bubblesort.bubblemain)
		
		displayfiles.button("Merge Sort",400,350,150,30,red,bright_red,mergesort.mergemain)
		displayfiles.button("Insertion Sort",400,400,150,30,red,bright_red,insertionsort.insertionmain)
	
		displayfiles.button("Quick Sort",400,450,150,30,red,bright_red,quicksort.quickmain)
	
		displayfiles.button("Quit",20,500,150,30,red,bright_red,visualQuit)	

		
	print("Out")
	pygame.quit()
	quit()
mainVisual()

