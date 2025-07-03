import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black=(0,0,0)
    obj=pygame.time.Clock()

    asteroids=pygame.sprite.Group()
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)

    aster_f=AsteroidField()

    player=Player(x = SCREEN_WIDTH / 2,y = SCREEN_HEIGHT / 2)
    dt=0

    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill(black)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        obj.tick(60)
        dt=obj.tick(60)/1000
    

if __name__ == "__main__":
    main()