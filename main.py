import pygame
from screen import Screen
from camera import Camera
from utils import D3Point, D3Angle, D2Point
from shapes import Triangle, Shape, Cube


pygame.init()


SCREEN_SIZE = (500, 500)

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CLOCK = pygame.time.Clock()
FPS = 60


CAMERA = Camera(
    D3Point(0, 0, 0),
    D3Angle(0, 0, 0),
    D3Point(0, 0, 4)
)
"""
TRIANGLE1 = Triangle(
    D3Point(0, 20, 50),
    D3Point(-20, 0, 50),
    D3Point(0, -20, 50),
    False,
    (100, 255, 0)
)
TRIANGLE2 = Triangle(
    D3Point(10, 20, 50),
    D3Point(10, 0, 100),
    D3Point(10, -20, 50),
    False,
    (0, 100, 255)
)
"""

CUBE = Cube(
    D3Point(5, 5, 50),
    10
)

DISPLAY = Screen(
    SCREEN,
    CAMERA,
    D2Point(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2),
    CUBE
)

D_FACTOR = 0.2


running = True
SCREEN.fill((255, 255, 255))
while running:
    SCREEN.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    if keys[pygame.K_p]:
        DISPLAY.camera.rotate(0, 0.01, 0)
    if keys[pygame.K_o]:
        DISPLAY.camera.rotate(0, -0.01, 0)
    if keys[pygame.K_z]:
        DISPLAY.camera.position.z += D_FACTOR
    if keys[pygame.K_s]:
        DISPLAY.camera.position.z -= D_FACTOR
    if keys[pygame.K_q]:
        DISPLAY.camera.position.x -= D_FACTOR
    if keys[pygame.K_d]:
        DISPLAY.camera.position.x += D_FACTOR
    DISPLAY.draw()
    CLOCK.tick(FPS)
    pygame.display.update()

pygame.quit()