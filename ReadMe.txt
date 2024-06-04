Game 2048

This is a Python implementation of the game 2048.

INTRODUCTION
2048 a simple 1-player board game. The goal of this game is to merge tiles with the same number into a single tile with the number 2048. The user can press the arrow keys in their keyboards to shift the tiles up, down, left and right. So that all the tiles will move to that direction and tiles with the same number will combine into a single tile with twice the value. The game will be ended when 2048 is reached, or all the tiles of the grid are occupied, and shifting does not create any space. Score will be recorded updated every time there is a merge on the grid with the value merged, and user can restart or end the game at any time they want by following the given instructions. 

DESIGN
1.	File name - Play Game.py
This file contains the main function to run the game by collectively calling the pre-defined classes and functions in the same repository, including GameBoard.py, Numbers.py, and MoveKeys.py. The main function uses try block to call the other predefined classes and functions to ask for the user input on the size of the grid (>= 4), display the turtle graphics with class GameBoard, keep listening for commands from the keyboard with class Movekeys, and implement updating the numbers on the grid with class Numbers. ValueError will be caught and printed to the console.
	
2.	File name - GameBord.py
This file contains class GameBoard, methods including,
1.	constructor __init__
2.	helper method draw_rectangle
3.	helper method turtle_matrix
4.	helper method instructions_and_score
5.	method display
The class is to draw the game board, and display it on the turtle canvas where user can play the game with keyboard. Elements on the game board includes, 
1.  a square board with n * n cells (squares)
2.	display the board with different colors per the number assigned to each cell
3.  display the number of each cell, except for 0
4.  display the score the user got, the instructions of how to restart, end the game and move the cells on the left side of the canvas
5.  print message on the canvas when user reaches number 2048, end the game, and raise ValueError to stop running the program, "You win the game!" printed to the console.
6.  print message on the canvas when user runs out of blank cells and merge cannot create new blank space, end the game, and raise ValueError to stop running the program, "You lose the game!" printed to the console.


3.  File name – Numbers.py
	This file contains class Numbers, methods including,
1.	constructor __init__
2.	helper method random_pair_generator
3.	helper method coordinate_matrix
4.	initialize_number_dictionary
5.	helper method keys_nested_list
6.	helper method move_numbers
7.	method shift_processor
8.	method dictionary_postshift
This class is to 
1.	generate, update and return number dictionary, which consists of n * n items, coordinates as keys and number 0 as values. Also initialize and update the score which comes from the merged numbers. Initialize and update the attribute gameover and win
2.	randomly pick two or three keys and assign them with value 2 or 4
3.	update the dictionary when the user shifts all the numbers to left / right / up / down
4.	merge the cells with the same value (no other number in between) in the same row / column and placed to the left cell for direction "left", similar logic for direction "right", "up" and "down"
5.  update the score with the merged value
6.  if there are still keys with value zero, randomly pick a key with value 0 and assign it with value 2 or 4, otherwise, gameover = True
7.  if there’s value = 2048, win = True

4.  File name – MoveKeys
	This file contains class MoveKeys, methods including,
1.	constructor __init__
2.	helper method move_up
3.	helper method move_down
4.	helper method move_right
5.	helper method move_left
6.	helper method end_game
7.	helper method restart_game
8.	helper method invalid_input_warning
9.	method bind_keyboard 
This class is to make turtle listen for the keyboard inputs, then use the pre-defined class to process the respective movement, including UP, DOWN, LEFT, RIGHT, E and R in turtle, indicating move all numbers up, down, left, right, end the game and restart the game respectively. The class will also print message, asking the user try again when invalid input (keys other than the four directions, E and R) is pressed during the game.

5.  File name – TestNumbers
	This file contains class TestNumbers, methods including,
1.	method setup to set up attributes and variable that are needed for the test 
2.	method test_constructor
3.	method test_initialize_number_dictionary
4.	method test_shift_processor
5.	method test_dictionary_postshift
This class is to use unittest to test the main methods of class Numbers

PROGRAM FEATURES
1.	This program allows user input as parameter for the size of the grid in a dialog before new game starts, notifying the minimum size is 4. The program will keep asking for the user input if invalid user input is given, i.e. input is less than 4, or input is not a number
2.	This program can automatically adjust the size of the gameboard according to the size input
3.	This program can implement the game without crushing, including,
a)	Ask for the size, and display the grid in the size the user asked for 
b)	User will be asked to re-type size in the dialog when invalid user input is typed in, i.e. non-number input, or any number < 4, size in float will be converted to integer without rounding.
c)	Start the game with 2 or 3 numbers (2 or 4) in the cell, highlighting with different color when cells merge. 
d)	Score is always tracked and updated on the canvas when two cells merge
e)	Instructions on how to end, restart the game, and move the cells is always clearly visible on the screen
f)	Shift all numbers up, down, left, right to the farthest blank cell without jumping over another number
g)	When shift left, if two cells in the same row shift next to each other and they both have the same number, the numbers are merged and placed in the cell that is on the left. Similar logic applies to shift right, up and down.
h)	A new number with value 2 or 4 comes in an empty cell in the grid post shift
i)	There’s a way to end the game at any time by pressing E
j)	There’s a way to restart the game at any time without having to exit and rerun the game by pressing R. The game will restart from asking for user input on size.
k)	There’s clear message on the canvas when 2048 is reached, the game will then end with winning message printed to the console.
l)	There’s clear message on the canvas when the game is over (all the cells are occupied and shifting does not create any space), the game will then end with losing message printed to the console.
m)	If the user press keys other than what the game uses, the program will ask the user to give valid input – keys including four directions, E and R.

GETTING STARTED
1.	To run the game, the user needs to have Python 3 installed, which can be download from the official website https://www.python.org/downloads/
2.	Once Python is installed, all the python files in the repository can be opened, open Play Game.py file to start the game. The user also needs to install the 'turtle' module, which is included with most Python installations.

HOW TO PLAY
1.	When start the game, the user will see a dialog popped out on the screen asking for the size of the grid, simply type in the size of the game board and a grid of tiles with 2 or 3 random numbers will be shown on the canvas. Note, the game only accepts size greater than 3, the game will not start with non-number input, or number < 4 . Size in float will be automatically converted to integer without rounding. 
Score will be updated whenever there's a merge with the value merged, as well as instructions to end, restart the game and how to move the cells.
2.	To move the tiles, use the arrow keys on the keyboard - press the 'UP' arrow to move the tiles up, the 'DOWN' arrow to move them down, the 'LEFT' arrow to move them left, and the 'RIGHT' arrow to move them right.
When shift the tiles, any tiles with the same number will be merged into a single tile with twice the value. For example, if you shift left, two tiles with number 2 in the same row without a different number in between will be combined and become a single tile to the left with number 4, and the score will be added by 4 at the same time. Same logic is applied to shift right, down and up.
3.	Cells will be highlighted with a different color whenever there is a merge
4.	User will win the game when any tile of the grid has the number 2048, and the game will be ended. The message "You got 2048!" will appear on the canvas for 1 second, then the game will end with the canvas closed, as well as a message "You win the game!" printed to the Turtle console.
5.	User will lose the game when the board is full and no more moves can be made to generate empty space, and the game will be ended. The message "GAME OVER" will display on the canvas for 1 second, then the game will end with the canvas closed, as well as a message "You lose the game!" printed to Turtle console.
6.	During the game, user can exit the game by pressing 'E'.
7.	User can restart the game from step 1 by pressing 'R'.
8.	There would be message on the screen showing “Invalid input, please try again!” when invalid keys are pressed during the game, invalid inputs including any other keys except for four arrow keys, E and R during the game.

ACKNOWLEDGEMENTS
This game was inspired by the original 2048 game https://play2048.co/. The Python implementation was created by Yun Lu.




