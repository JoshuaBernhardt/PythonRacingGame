import pygame      #import
pygame.init()      #Initialise
gameRunning=True   #gameRunning
pygame.display.init()


screen=pygame.display.set_mode((1200,1080),0) #Set display res
pygame.display.set_caption("Game")   #Set caption to game
car=pygame.image.load("Car.png")     #Load assets
carRect=car.get_rect()
    
class Car(pygame.sprite.Sprite):

    def __init(self,width,height):
        super().__init__()

        self.image=car
