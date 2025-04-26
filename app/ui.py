import pygame

def show_instructions(screen):
    """Display instruction text and wait for key press to start."""
    font = pygame.font.Font(None, 36)
    text = font.render('Press any key to start tapping with the beat.', True, (255, 255, 255))
    text_rect = text.get_rect(center=(300, 200))
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
