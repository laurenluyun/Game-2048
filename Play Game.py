'''
CS5001
2023Spring
Project: 2048 - Play Game
Yun Lu
This program is to run the game of 2048 by calling the pre-defined
classes, including GameBoard, Numbers and MoveKeys. The program will
firstly ask for user input about the size of the game board in a dialog,
and start the game on turtle canvas, where user can play the game by
pressing specific keys on the keyboard, including arrow keys - left, right,
up and down, as well as E (end the game) and R (restart the game).
Example:
    1. user input 4 as the size of the game board in the dialog popped out
    2. a 4 * 4 grids will display on the canvas, with instructions of
    ending and restarting the game and score on the left side of the
    canvas, and 2 or 3 grids showing numbers of 2 or 4. Each cell will
    display different color based on the number in it.
    3. all the numbers will move to left when user press left arrow,
    and cells with the same number in the same row with no other numbers
    in between will merge and placed in the cell that is on the left,
    similar logic for moving right, up and down.
    4. when two cells merge, the value that is created is added to the
    score of the user
    5. value with 2 or 4 will be created in a random blank cell post
    each movement
    6. The game will end when all the cells of the grid are occupied,
    and shifting does not create any space. the message "GAME OVER" will
    display on the canvas for 1 second, then the game will end with the
    canvas closed, as well as a message "You lose the game!" printed to
    Turtle console.
    7. if there's number 2048 in one of the cells, the message "You got
    2048!" will appear on the canvas for 1 second, then the game will end
    with the canvas closed, as well as a message "You win the game!"
    printed to the Turtle console.
    8. the game will restart from step 1 when user press R
    9. the game will end and the canvas will be closed when user press E
    10. User will be asked to re-type size in the dialog when invalid user
    input is typed in, i.e. non-number input, or any number < 4, size in
    float will be converted to integer without rounding.
    11. There will be message on the canvas showing invalid input when any
    other inputs from the keyboard pressed, except for four arrow keys,
    E and R during the game.
'''

from GameBoard import GameBoard
from Numbers import Numbers
from MoveKeys import MoveKeys
import turtle

def main():
    # try block to start the game by asking user input about the size
    # of the grid
    try:
        # use the numinput() function to get size of the board from the
        # user with a dialog, minium input is 4
        size_string = turtle.numinput("Enter the size of the board: \n",
                                      "(at least 4)", minval = 4)
        # call the class Gameboard
        my_board = GameBoard(size_string)
        # get the size from the attribute of my_board and save in a variable
        size = my_board.size
        # get the initialized number dictionary and saved in a variable
        number_dictionary = Numbers(size).initialize_number_dictionary()
        # get the initialized score and saved in a variable
        score = Numbers(size).score
        # generate the attribute gameover and win from Numbers and pass to
        # my_board
        gameover = Numbers(size).gameover
        win = Numbers(size).win
        # display the initialized game board, numbers, scores and instruction
        # on the canvas
        my_board.display(number_dictionary, score, gameover, win)
        # call the MoveKeys class to keep listening for keys pressed and
        # implement moving tiles, end / restart the game
        move_keys = MoveKeys(size, number_dictionary)
        # keep listening for user input - arrow keys, E and R, until the game
        # is ended
        move_keys.bind_keyboard()
    # print error message when ValueError is raised
    except ValueError as ex:
        print(ex)

if __name__ == '__main__':
    main()