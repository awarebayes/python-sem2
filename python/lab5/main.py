import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()


from scene import all_sprites

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    all_sprites.update()
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
