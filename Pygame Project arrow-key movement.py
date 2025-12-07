import pygame
pygame.init()

screen_w = 640
screen_h = 640

screen = pygame.display.set_mode((screen_w, screen_h))

pygame.display.set_caption("Adding Sprites")

block_img = pygame.image.load("/Applications/kenney_tiny-dungeon/Tiles/tile_0007.png")
dimensions = block_img.get_rect()


sprite_positions = []

running = True
clock = pygame.time.Clock()

x = 320 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (x - 10 > 0):
        x -= 10
    if keys[pygame.K_RIGHT] and (x + 10 < 640):
        x += 10
            
    screen.fill((255,255,255))

    dimensions.center = (x, 320)
            
    screen.blit(block_img, dimensions)
    
    clock.tick(60)
        
    pygame.display.flip()
    


    

pygame.quit()
