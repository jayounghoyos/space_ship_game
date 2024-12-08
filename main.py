import pygame

# general setup
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("space Shooter")
running = True

#surface
surf = pygame.Surface((100,200))


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    display_surface.fill("white")
    display_surface.blit()
    pygame.display.update()

pygame.quit()
