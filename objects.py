import pygame

SCREEN = WIDTH, HEIGHT = 500, 650

class Background():
    def __init__(self, display):
        self.display = display
        
        self.image = pygame.image.load('Assets/background.jpg')
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        
        self.reset()
        self.move = True
        
    def update(self, speed):
        if self.move:
            self.y1 += speed
            self.y2 += speed
            
            if self.y1 >= HEIGHT:
                self.y1 = -HEIGHT
            if self.y2 >= HEIGHT:
                self.y2 = -HEIGHT
                
        self.display.blit(self.image, (self.x, self.y1))
        self.display.blit(self.image, (self.x, self.y2))
        
    def reset(self):
        self.x = 0
        self.y1 = 0
        self.y2 = -HEIGHT 
        
class UFO:
    def __init__(self, x, y):
        self.image = pygame.image.load('Assets/ufo.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect(center=(x,y))
        
    def update(self):
        pass
    
    def draw(self, display):
        display.blit(self.image, self.rect)