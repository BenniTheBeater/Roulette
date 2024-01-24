import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

# Create the window
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Roulette Wheel")

# Font setup
font = pygame.font.SysFont(None, 30)

def get_color(number):
    if number == 0:
        return GREEN
    elif number >= 1 and number <= 10:
        return RED if number % 2 != 0 else BLACK
    elif number >= 11 and number <= 18:
        return BLACK if number % 2 != 0 else RED
    elif number >= 19 and number <= 28:
        return RED if number % 2 != 0 else BLACK
    elif number >= 29 and number <= 36:
        return BLACK if number % 2 != 0 else RED
    else:
        return None

def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    win.blit(text_surface, (x, y))

def main():
    running = True
    number_text = ''

    while running:
        win.fill(WHITE)
        draw_text("Enter a number (0-36): " + number_text, 50, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        number = int(number_text)
                        color = get_color(number)
                        if color is not None:
                            result_text = f"Number {number} is {color}"
                            draw_text(result_text, 50, 100)
                            pygame.display.update()
                        else:
                            draw_text("Error: Number not between 0-36", 50, 100)
                            pygame.display.update()
                    except ValueError:
                        draw_text("Error: Invalid input", 50, 100)
                        pygame.display.update()
                    number_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    number_text = number_text[:-1]
                else:
                    number_text += event.unicode

if __name__ == "__main__":
    main()