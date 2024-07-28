import pygame
import random
import time
import sys
import os
from pygame import mixer

mixer.init()

victory = mixer.Sound("sound/victory.mp3")
lose = mixer.Sound("sound/lose.mp3")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30
ARROW_SIZE = 100
ARROW_SPACING = 20
BG_COLOR = (105, 131, 218)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 50)
INPUT_FONT = pygame.font.Font(None, 36)

# Loading photos
trophy_image = pygame.image.load("photos/trophy.png")
you_lose_image = pygame.image.load("photos/you_lose.png")

# Scaling photos
trophy = pygame.transform.scale(trophy_image, (100, 100))
you_lose = pygame.transform.scale(you_lose_image, (150, 150))

# Arrow images
ARROW_IMAGES = {
    "up": pygame.image.load("photos/up.jpg"),
    "down": pygame.image.load("photos/down.jpg"),
    "left": pygame.image.load("photos/left.jpg"),
    "right": pygame.image.load("photos/right.jpg"),
}

# Function returns string that shows whether player won or lost.
def text(i, time = None):
    if i == True:
        return FONT.render(f"Correct!  Time: {time} seconds.", True, "Green")
    
    else:
        return FONT.render("Incorrect!", True, (150, 0, 0))

# Function that Generates a random sequence of arrows
def generate_sequence(length=6):
    return [random.choice(["up", "down", "left", "right"]) for _ in range(length)]

# Function that displays arrows on screen
def display_sequence(screen, sequence, start_time):
    screen.fill(BG_COLOR)
    for i, direction in enumerate(sequence):
        image = pygame.transform.scale(ARROW_IMAGES[direction], (ARROW_SIZE, ARROW_SIZE))
        screen.blit(image, (i * (ARROW_SIZE + ARROW_SPACING) + 50, 50))
    pygame.display.flip()


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Keyboard Reflex Game")
    clock = pygame.time.Clock()

    sequence = generate_sequence()
    user_input = []
    start_time = time.time()

    while True:
        screen.fill(BG_COLOR)
        display_sequence(screen, sequence, start_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    user_input.append("up")
                elif event.key == pygame.K_DOWN:
                    user_input.append("down")
                elif event.key == pygame.K_LEFT:
                    user_input.append("left")
                elif event.key == pygame.K_RIGHT:
                    user_input.append("right")

        # Display user input
        input_text = INPUT_FONT.render("Your Input: " + " ".join(user_input), True, TEXT_COLOR)
        screen.blit(input_text, (50, HEIGHT - 100))


        # Check if user input matches the sequence
        win = False
        if len(user_input) == len(sequence):
            if user_input == sequence:
                win = True
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 2)
                result_text = text(win, elapsed_time)
                mixer.Sound.set_volume(victory, 0.1)
                mixer.Sound.play(victory)
                screen.blit(trophy, (350, 190))
            else:
                result_text = text(win)
                mixer.Sound.set_volume(lose, 0.1)
                mixer.Sound.play(lose)
                screen.blit(you_lose, (325, 160))
            screen.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, HEIGHT // 2))
            screen.blit(FONT.render("Press any key to retry.", True, TEXT_COLOR), (220, 400))
            pygame.display.flip()

            # Wait for user to retry
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        sequence = generate_sequence()
                        user_input = []
                        start_time = time.time()
                        waiting = False
                clock.tick(FPS)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
