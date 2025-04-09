import pygame
from constants import *

def main():
    #initialize pygame
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =pygame.time.Clock()
    dt = 0
    #created game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #limit fps
        dt = clock.tick(60) /1000
        screen.fill("black")
        pygame.display.flip()






if __name__ == "__main__":
    main()