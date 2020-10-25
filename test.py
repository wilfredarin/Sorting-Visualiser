import pygame
import random 



a = []
for i in range(100):
	a.append(random.randint(1,100))
print(a)



x = pygame.init()
display_width = 800
display_height  = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
speed = 30




def visualiseSort():
	
	gameDisplay.fill((233,233,233))
	displayArray(a,0)
	pygame.display.update()

	closed = False
	while not closed:
		# pygame.display.update()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				closed = True 
		# bubleSort(a)
		# insertionSort(a)
		mergeSort(a)
		#quickSort(a)
		q = input()
		if q=="q":
			closed = True
		# displayArray(a,0)

		pygame.display.update()









### Sorting Algos ###


###
def bubleSort(a):
	for i in range(len(a)):
		for j in range(len(a)-i-1):
			if a[j]>a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					closed = True
					exit()
			gameDisplay.fill((233,233,233))
			displayArray(a,j)
			pygame.display.update()
			clock.tick(speed)
			



####

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
			gameDisplay.fill((0,0,0))
			displayArray(a,j)
			pygame.display.update()
			clock.tick(speed)
			a[j+1] = a[j]
			j-=1 
		a[j+1] = place_key 








# quickSort(a)
print(a)









def lines(lx,ly,lw,h,color):
	pygame.draw.rect(gameDisplay,color,[lx,ly,lw,h])

def displayArray(a,j=0):
	for i in range(len(a)):
		if i==j:
			lines(200+i*2,10,2,a[i]*5,(255,0,0))
		elif i%2==0:
			lines(200+i*2,10,2,a[i]*5,(0,55,244))
		else:
			lines(200+i*2,10,2,a[i]*5,(0,255,0))

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
			gameDisplay.fill((0,0,0))
			displayArray(a,k)
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



###
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
			gameDisplay.fill((0,0,0))
			displayArray(a,j)
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




visualiseSort()



