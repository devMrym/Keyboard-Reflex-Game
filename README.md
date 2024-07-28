# KEYBOARD REFLEX GAME
## Video Demo:
###  <https://youtu.be/M6Et9dG_5Jo>
## Description:
#### The objective of the game is to test the player's reflexes and typing speed by requiring them to replicate a random sequence of arrow keys displayed on the screen. The player must correctly input the sequence using their arrow keys on their keyboard. 


#### The main library used to help develop this project was Pygame. Other libraries used were:
- random: to generate the random sequence of arrow key images.
- time: to calculate how long it took the user to input the correct keys in order.
- sys: to exit the program
- os: to solve the "FileNotFoundError: No such file or directory" Error

## Functions in project.py:
- `main()`: The main function that initializes the game and handles the game loop.
- `generate_sequence(length=6)`: Generates a random sequence of arrow keys.
- `display_sequence(screen, sequence, start_time)`: Displays the sequence of arrows on the screen.
- `text(is_correct, time=None)`: Returns a Pygame Surface with the result text based on whether the player's input was correct.

## Features:
- Sequence Display: The game generates and displays a random sequence of arrow keys.
- User Input: Players input the sequence using arrow keys on the keyboard.
- Feedback: The game provides visual and audio feedback based on the player's performance.
- Victory: Displays a trophy image and plays a victory sound.
- Loss: Displays an "X" image and plays a loss sound.
- Retry Option: After completing a round, players can press any key to start a new game with a fresh sequence.

## Assets:
- Sound:
  - sound/victory.mp3
  - sound/lose.mp3
- Images:
  - photos/trophy.png
  - photos/you_lose.png
  - photos/up.jpg
  - photos/down.jpg
  - photos/left.jpg
  - photos/right.jpg

## My thought process during this project:

 After finishing all the CS50P lectures, I was super excited to get started on the final project. At first, I considered doing a simple terminal-based project However, after taking a look at some of the projects in the Gallery of Final Projects, I stumbled upon a student using Pygame and was inspired to aim a bit higher. I had to follow a lengthy YouTube tutorial to understand how Pygame is implemented. I also found lots of helpful posts on StackOverflow and Reddit when dealing with errors I didn't understand.Once I completed the basic functions of the game, I felt like something was missing. I decided to add a couple of photos and sound effects to make it more interesting. Scaling the photos and searching for the sound effects felt like a whole other challenge, but it looked pretty decent in the end, so I'm not complaining. I really enjoyed every part of making this, and I was even happier when some of my family members tried it out and pushed themselves to get the least amount of time.
 ### THANK YOU!
