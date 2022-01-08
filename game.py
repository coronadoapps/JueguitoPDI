import pygame 
from objects import Background, UFO

pygame.init()
SCREEN = WIDTH, HEIGHT = 500, 650

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

pygame.display.set_caption('Jueguito')
if width >= height:
    display = pygame.display.set_mode(SCREEN)
else:
    display = pygame.display.set_mode(SCREEN, pygame.SCALED | pygame.FULLSCREEN)

bg = Background(display)
p = UFO(250, HEIGHT - 80)

fps = 60
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                run = False
                
    bg.update(3)
    p.draw(display)
    pygame.display.update()