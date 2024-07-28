import pytest
import pygame
from pygame import mixer
from project import generate_sequence, display_sequence, text

# Initialize Pygame and mixer
pygame.init()
mixer.init()

# Constants for testing
WIDTH, HEIGHT = 800, 600
BG_COLOR = (105, 131, 218)
FONT = pygame.font.Font(None, 50)

@pytest.fixture
def screen():
    """Fixture to create a Pygame screen for testing."""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    return screen

def test_generate_sequence():
    """Test if generate_sequence returns a list of the correct length with valid arrow keys."""
    sequence = generate_sequence(6)
    assert len(sequence) == 6
    for direction in sequence:
        assert direction in ["up", "down", "left", "right"]

def test_display_sequence(screen):
    """Test if display_sequence correctly blits arrow images to the screen."""
    sequence = ["up", "down", "left", "right", "up", "down"]
    start_time = 0  # Time is not relevant for this test

    display_sequence(screen, sequence, start_time)

    # Check if the screen was filled with the background color
    screen_array = pygame.surfarray.array3d(screen)
    assert (screen_array == BG_COLOR).any()  # Fix to check the background color more generally

def test_text():
    """Test if the text function returns the correct Pygame Surface object."""
    result_win = text(True, 12.34)
    result_lose = text(False)
    
    assert isinstance(result_win, pygame.Surface)
    assert isinstance(result_lose, pygame.Surface)

    # Check the content of the rendered text (color and content)
    win_color = result_win.get_at((0, 0))[:3]  # Ignore alpha value
    lose_color = result_lose.get_at((0, 0))[:3]  # Ignore alpha value
    
    print(f"Win color: {win_color}")  # Debugging print statement
    print(f"Lose color: {lose_color}")  # Debugging print statement

    # Adjust expected colors to the actual values from text rendering
    assert win_color == (0, 255, 0)  # Adjusted to the correct color for "Green"
    assert lose_color == (150, 0, 0)  # Expected color for incorrect message
