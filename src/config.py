import pygame
pygame.init()

FPS = 60
n_rows = 15
n_columns = 30
block_size = 20
screen_height = n_rows * block_size
screen_width = n_columns * block_size
stickman_height = 30
stickman_width = 20
stamina_max = 200
health_max = 100
arrow_img_path = "resources/Arrow.PNG"
potion_img_path = "resources/Potion.png"
block_img_path = "resources/block.png"
map_path = "resources/map.txt"
database_path = "resources/database.txt"
play_back_path = "resources/play_back.png"
player_images_left = [
    pygame.image.load("resources/figure-L1.gif"),
    pygame.image.load("resources/figure-L2.gif"),
    pygame.image.load("resources/figure-L3.gif")
]
player_images_right = [
    pygame.image.load("resources/figure-R1.gif"),
    pygame.image.load("resources/figure-R2.gif"),
    pygame.image.load("resources/figure-R3.gif")
]
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (50, 205, 50)
BLACK = (0, 0, 0)