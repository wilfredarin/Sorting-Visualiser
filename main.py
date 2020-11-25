import pygame
import visual_main
# import displayfiles
# import bubblesort
# import insertionsort
# import mergesort
# import quicksort

pygame.init()

red = (200,0,0)
green = (0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
white = (255,255,255)



screen_width,screen_height = 800,600
screen = pygame.display.set_mode([screen_width, screen_height])



visual_main.mainVisual()

pygame.quit()
quit()