'''
CS5001
2023Spring
Project: 2048 - MoveKeys
Yun Lu
This program is to use the pre-defined class to process the key movement in
turtle, including press UP, DOWN, LEFT, RIGHT, E and R, indicating move
all numbers up, down, left, right, end the game and restart the game
respectively.
Example:
    1. a game board would be drawn with n * n cells, where there would be
    numbers (2 or 4) within some cells, each cell with specific color based on
    the number in the cell
    2. on the left side of the canvas, there are three boxes
    indicating the instruction of 1. how to restart the game 2. end the
    game 3. the score the user got while playing the game
    3. the game board will be updated every time user press UP, DOWN,
    LEFT or RIGHT, the game will end when E is pressed, and will restart
    when R is pressed
    4. the game will display the message when 2048 is reached in the cell,
    then the game will end, ValueError will be raised to stop the program.
    "You win the game!" printed to the console.
    5. the game will show message when no blank cell is available or to be
    merged, then the game will end, ValueError will be raised to stop the
    program, "You lose the game!" printed to the console.
    6. there will be message showing "Invalid input please try again" on
    the canvas when there's any other input pressed other than the four
    directions and E, R
'''

import turtle
from GameBoard import GameBoard
from Numbers import Numbers

class MoveKeys():
    '''
    class: MoveKeys
    This class is to make turtle listen for the keyboard inputs, then use the
    pre-defined class to process the respective movement, including UP, DOWN,
    LEFT, RIGHT, E and R in turtle, indicating move all numbers up, down, left
    , right, end the game and restart the game respectively. There will be
    messages showing on the canvas telling user to try again when invalid
    input is pressed, other than the four direcitons and E, R.
    '''
    def __init__(self, size, number_dictionary):
        '''
        Constructor: generate attributes for the object
        parameter:
            size: size of the game board, n * n, integer
            number_dictionary: dictionary with coordinates as keys, number
                as value
        return: none
        '''
        # generate the size attribute of the object
        self.size = size
        # call number class and save the object as attribute
        self.my_number = Numbers(self.size)
        # add the initialized number dictionary as an attribute to be updated
        self.dictionary = number_dictionary

    def move_up(self):
        '''
        method: move_up
        purpose: this method is to use pre-defined class / function to update
            the number dictionary and the score when the user pressed UP
            key in the keyboard with object my_number and then use the
            Gameboard to display the game board, updated dictionary,
            messages, and score on the canvas.
        parameter: none
        return: draw the game board, display the updated number dict,
            score, instructions, and messages, print error message when
            there's ValueError
        '''
        # try block to execute the up movement
        try:
            # update the dictionary attribute after shift numbers up
            self.dictionary = self.my_number.shift_processor(self.dictionary,
                                                             "up")
            # update the dictionary attribute post shift
            self.dictionary = self.my_number.dictionary_postshift(
                self.dictionary)
            # get the score attribute from my_number and saved in variable
            score = self.my_number.score
            # get the win attribute from my_number and saved in variable
            win = self.my_number.win
            # get the gameover attribute from my_number and saved in variable
            gameover = self.my_number.gameover
            # display the whole game board with the updated dict and score
            GameBoard(self.size).display(self.dictionary, score, gameover,
                                         win)
        # print error message when ValueError is raised
        except ValueError as ex:
            print(ex)

    def move_down(self):
        '''
        method: move_down
        purpose: this method is to use pre-defined class / function to update
            the number dictionary and the score when the user pressed DOWN
            key in the keyboard with object my_number and then use the
            Gameboard to display the game board, updated dictionary,
            messages, and score on the canvas.
        parameter: none
        return: draw the game board, display the updated number dict,
            score, instructions, and messages, print error message when
            there's ValueError
        '''
        # try block to execute the down movement
        try:
            # update the dictionary attribute after shift numbers down
            self.dictionary = self.my_number.shift_processor(self.dictionary,
                                                           "down")
            # update the dictionary attribute post shift
            self.dictionary = self.my_number.dictionary_postshift(
                self.dictionary)
            # get the score attribute from my_number and saved in variable
            score = self.my_number.score
            # get the win attribute from my_number and saved in variable
            win = self.my_number.win
            # get the gameover attribute from my_number and saved in variable
            gameover = self.my_number.gameover
            # display the whole game board with the updated dict and score
            GameBoard(self.size).display(self.dictionary, score, gameover,
                                         win)
        # print error message when ValueError is raised
        except ValueError as ex:
            print(ex)

    def move_right(self):
        '''
        method: move_right
        purpose: this method is to use pre-defined class / function to update
            the number dictionary and the score when the user pressed RIGHT
            key in the keyboard with object my_number and then use the
            Gameboard to display the game board, updated dictionary,
            messages, and score on the canvas.
        parameter: none
        return: draw the game board, display the updated number dict,
            score, instructions, and messages, print error message when
            there's ValueError
        '''
        # try block to execute the right movement
        try:
            # update the dictionary attribute after shift numbers right
            self.dictionary = self.my_number.shift_processor(self.dictionary,
                                                             "right")
            # update the dictionary attribute post shift
            self.dictionary = self.my_number.dictionary_postshift(
                self.dictionary)
            # get the score attribute from my_number and saved in variable
            score = self.my_number.score
            # get the win attribute from my_number and saved in variable
            win = self.my_number.win
            # get the gameover attribute from my_number and saved in variable
            gameover = self.my_number.gameover
            # display the whole game board with the updated dict and score
            GameBoard(self.size).display(self.dictionary, score, gameover,
                                         win)
        # print error message when ValueError is raised
        except ValueError as ex:
            print(ex)

    def move_left(self):
        '''
        method: move_left
        purpose: this method is to use pre-defined class / function to update
            the number dictionary and the score when the user pressed LEFT
            key in the keyboard with object my_number and then use the
            Gameboard to display the game board, updated dictionary,
            messages, and score on the canvas.
        parameter: none
        return: draw the game board, display the updated number dict,
            score, instructions, and messages, print error message when
            there's ValueError
        '''
        # try block to execute the left movement
        try:
            # update the dictionary attribute after shift numbers left
            self.dictionary = self.my_number.shift_processor(self.dictionary,
                                                             "left")
            # update the dictionary attribute post shift
            self.dictionary = self.my_number.dictionary_postshift(
                self.dictionary)
            # get the score attribute from my_number and saved in variable
            score = self.my_number.score
            # get the win attribute from my_number and saved in variable
            win = self.my_number.win
            # get the gameover attribute from my_number and saved in variable
            gameover = self.my_number.gameover
            # display the whole game board with the updated dict and score
            GameBoard(self.size).display(self.dictionary, score, gameover,
                                         win)
        # print error message when ValueError is raised
        except ValueError as ex:
            print(ex)

    def end_game(self):
        '''
        method: end_game
        purpose: this method is to close the window when the user pressed E
        parameter: none
        return: close the turtle window
        '''
        # close the window
        turtle.bye()

    def restart_game(self):
        '''
        method: restart_game
        purpose: this method is to use the Gameboard to restart the
            game, ask user input for size, display the game board,
            instructions, initialized dictionary, messages and score on the
            canvas, and then continue the game by calling the class MoveKeys
        parameter: none
        return: display the game board, instructions, initialized dictionary
            , messages and score on the canvas, then continue the game by
            calling the Movekeys class
        '''
        # try block to restart the game
        try:
            # clear the whole canvas first before restarting the game
            turtle.Screen().clear()
            # use the numinput() function to get size of the board from the
            # user with a dialog
            size_string = turtle.numinput("Enter the size of the board: "
                                          "\n", "(at least 4)", minval = 4)
            # call the class Gameboard
            my_board = GameBoard(size_string)
            # get the size and saved in a variable
            size = my_board.size
            # get the initialized number dictionary and saved in a variable
            number_dictionary = Numbers(size).initialize_number_dictionary()
            # get the score attribute from my_number and saved in variable
            score = self.my_number.score
            # get the gameover attribute from my_number and saved in variable
            gameover = self.my_number.gameover
            # get the win attribute from Number and saved in variable
            win = self.my_number.win
            # display the whole game board with the updated dict and score
            my_board.display(number_dictionary, score, gameover, win)
            # continue the game by calling the class Movekeys
            move_keys = MoveKeys(size, number_dictionary)
            # call the bind_keyboard method to react to the user input
            move_keys.bind_keyboard()

        # print error message when ValueError is raised and close the canvas
        except ValueError as ex:
            print(ex)

    def invalid_input_warning(self):
        '''
        method: invalid_input_warning
        purpose: this method is to print message on the canvas when there's
            invalid input from the user
        parameter: none
        return: message printed on the canvas "The input is invalid!"
        '''
        turtle.hideturtle()
        turtle.color("black")
        turtle.goto(-400, 30)
        # write and update the message when there's invalid input from user
        turtle.write("The input is invalid\nPlease try again!", font = (
            "Arial", 15, "normal"))
        turtle.update()

    def bind_keyboard(self):
        '''
        method: bind_keyboard
        purpose: this method is to bind the keyboard inputs to the
            pre-defined methods above, including move_up, move_down,
            move_right, move_left, end_game, restart_game, and
            invalid_input_warning, and make turtle keep listening for
            keyboard inputs and keep window open until the user closes it
        parameter: none
        return: none
        '''
        # bind the keyboard inputs to the methods
        turtle.onkeypress(self.move_up, "Up")
        turtle.onkeypress(self.move_down, "Down")
        turtle.onkeypress(self.move_right, "Right")
        turtle.onkeypress(self.move_left, "Left")
        turtle.onkeypress(self.end_game, "E")
        turtle.onkeypress(self.restart_game, "R")
        turtle.onkeypress(self.invalid_input_warning)
        # start listening for keyboard inputs
        turtle.listen()
        # keep the turtle window open until the game is ended
        turtle.mainloop()