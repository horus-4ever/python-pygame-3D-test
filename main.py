import pygame
from screen import Screen
from camera import Camera
from utils import D3Point, D3Angle, D2Point
from shapes import Triangle, Shape, Cube, Chunk
import random


pygame.init()


SCREEN_SIZE = (500, 500)

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
CLOCK = pygame.time.Clock()
FPS = 120


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

"""CUBES = []
for i in range(100):
    for j in range(100):
        n = random.randint(-1, 1)
        CUBE = Cube(
            D3Point(i * 10, 5, 50 + j * 10),
            10
        )
        CUBES.append(CUBE)
"""
CHUNK = Chunk(
    D3Point(-2, 0, 40),
    2,
    10
)

CHUNKS = []
for i in range(10):
    for j in range(10):
        CHUNKS.append(Chunk(
            D3Point(i * 10 * 2, 5, 50 + j * 10 * 2),
            2,
            10
        ))

# CUBES = Shape(*CUBES)

DISPLAY = Screen(
    SCREEN,
    CAMERA,
    D2Point(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2),
    *CHUNKS
)

D_FACTOR = 0.2


running = True
while running:
    change = False
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    if keys[pygame.K_p]:
        DISPLAY.camera.rotate(0, 0.01, 0)
        change = True
    if keys[pygame.K_o]:
        DISPLAY.camera.rotate(0, -0.01, 0)
        change = True
    if keys[pygame.K_m]:
        DISPLAY.camera.rotate(0.01, 0, 0)
        change = True
    if keys[pygame.K_l]:
        DISPLAY.camera.rotate(-0.01, 0, 0)
        change = True
    if keys[pygame.K_z]:
        DISPLAY.camera.position.z += D_FACTOR
        change = True
    if keys[pygame.K_s]:
        DISPLAY.camera.position.z -= D_FACTOR
        change = True
    if keys[pygame.K_q]:
        DISPLAY.camera.position.x -= D_FACTOR
        change = True
    if keys[pygame.K_d]:
        DISPLAY.camera.position.x += D_FACTOR
        change = True
    if keys[pygame.K_SPACE]:
        DISPLAY.camera.position.y -= D_FACTOR
        change = True
    if keys[pygame.K_LSHIFT]:
        DISPLAY.camera.position.y += D_FACTOR
        change = True
    if change:
        SCREEN.fill((255, 255, 255))
        DISPLAY.draw()
    CLOCK.tick(FPS)
    pygame.display.update()

pygame.quit()