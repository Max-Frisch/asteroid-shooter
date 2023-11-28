import pygame

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
    # 1 get input -> events (mouse click, mouse movement, keypress on a button or controller or touchscreen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # 2 updates

    # 3 show the frame to the player / update the display surface
    pygame.display.update()
    