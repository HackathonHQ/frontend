import pygame
from gpiozero import Button
b = Button(2)
pygame.init()
my_sound = pygame.mixer.Sound('Downloads/Sky High.wav')

def hello():
   my_sound.play()
    
b.when_pressed = hello
