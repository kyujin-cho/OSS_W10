import pygame
# Loop until the user clicks the close button.
done = False

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption('CMSC 150 is cool')

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

bg_position = [0, 0]
# Image from http://ProgramArcadeGames
bg_image = pygame.image.load("image.jpg").convert()
player_image = pygame.image.load("player.png").convert()
# player_image.set_colorkey(BLACK)

# click_sound = pygame.mixer.Sound('./laser5.ogg')

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     click_sound.play()
    screen.blit(bg_image, bg_position)

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    
    # Copy image to screen:
    if x >= 44:
        x -= 44
    if y >= 30:
        y -= 30
    screen.blit(player_image, [x, y])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
