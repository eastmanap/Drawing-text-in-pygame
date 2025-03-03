import pygame
import sys
import colors
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object
    
    running = True
    while running:
        running = handle_events()
        screen.fill(colors.WHITE)  # Use color from config
        
        # Draw on the screen
        def draw_text(text, font, color, pos):
            img = font.render(text, True, color)
            screen.blit(img, pos)
        
        text_font = pygame.font.Font('Minecraft-Seven_v2.ttf', 100)
        draw_text('You Died!', text_font, colors.YOUTUBE_AD_RED, (175, 200))

        text_font2 = pygame.font.SysFont('Arial', 30)
        draw_text('Try again?', text_font2, colors.BLACK, (325, 350))
    
        pygame.display.flip()
        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
