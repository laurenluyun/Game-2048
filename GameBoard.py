'''
CS5001
2023Spring
Project: 2048 - GameBoard
Yun Lu
This program is to draw the game board, numbers, score, instructions and
messages and display it on the turtle canvas where user can play the game
with keyboard.
Example:
    1. a game board would be drawn with n * n cells, where there would be
    numbers (2 or 4) within some cells, each filled with specific color
    based on the number in the cell
    2. on the left side of the canvas, there are four boxes
    indicating the instruction of 1. how to restart the game 2. end the
    game 3. the score the user got while playing the game 4. how to move
    the cells
    3. the game board will be updated every time the numbers are moved /
    updated
    4. the game will show the user when 2048 is reached in the cell,
    and the game will end, meanwhile raise ValueError to stop running
    program, "You win the game!" printed to the console. Message "GAME
    OVER" will be printed on the canvas for 1 second, and the canvas will
    be closed, with ValueError raised, and "You lose the game" printed to
    the console when there's no blank cell
'''

import turtle
from turtle import Screen
import time

class GameBoard():
    '''
    class: Gameboard
    This class is to generate a game board and display all the elements
    required for the game 2048, including,
    1. a square board with n * n cells (squares)
    2. display the board with different colors per the number assigned to
    each cell
    3. display the number of each cell
    4. display the score the user got, the instructions of how to restart
    , end the game, and how to move the cells
    5. print message on the canvas when user reaches number 2048, end the
    game, and raise ValueError to stop running the program, "You win the
    game!" printed to the console. Print "GMAE OVER" for 1 second, end the
    game, ValueError raised with "You lose the game" printed to the console
    when there's no blank cell and shift does not create new space
    '''

    def __init__(self, size):
        '''
       Constructor: generate attributes for the object
       Parameters:
           size of the board, float which is larger than 4
        return: none
       '''
        # generate the size attribute of the game board
        self.size = int(size)
        # set up the screen size - length
        self.screen_length = 950
        # set up the screen size - length
        self.screen_height = 700
        # compute and store distance of each cell as attribute
        self.distance = 60

    def draw_rectangle(self, length, height, color):
        '''
        method: draw_rectangle
        purpose: helper method to draw a rectangle with specific length,
            height and color with turtle
        parameters:
            length: length of the rectangle to be drawn by turtle
            length: height of the rectangle to be drawn by turtle
            color: color to be filled in the rectangle by turtle, string
        return:
            a rectangle with specific length, height, and color drawn by
            turtle
        '''
        # start drawing
        turtle.pendown()
        # set the color of the rectangle to be drawn
        turtle.fillcolor(color)
        turtle.begin_fill()
        # for loop to draw the rectangle
        for i in range(2):
            turtle.forward(length)
            turtle.left(90)
            turtle.forward(height)
            turtle.left(90)
        turtle.end_fill()
        # stop drawing
        turtle.penup()
        # update the canvas with the rectangle drawn
        turtle.update()

    def turtle_matrix(self):
        '''
        method: turtle_matrix
        purpose: helper method to generate and return a nested list of turtle
        parameters: none
        return: an n * n matrix (n = self.size) in the form of nested list,
            containing n * n turtles as elements, at their respective
            coordinate, according to the size of the board
        '''
        # set an empty list to append turtles as elements
        turtle_matrix = []
        # for loop to append self.size number of rows
        for i in range(self.size):
            row = []
            # for loop to append self.size number of turtles in each row
            for j in range(self.size):
                # generate a turtle for each cell
                key = turtle.Turtle()
                # set the fastest speed
                key.speed(0)
                # Hide the arrow of the turtle
                key.hideturtle()
                # avoid draw anything on the anything
                key.penup()
                # set the location / coordinate of the turtle - left down
                # corner of each cell
                key.goto(j * self.distance - 200, i * self.distance - 200)
                # append the turtle to the row (list)
                row.append(key)
            # append the list of row to the nested list
            turtle_matrix.append(row)
        return turtle_matrix

    def instructions_and_score(self, x, y, text):
        '''
        method: instructions_and_score
        purpose: helper method to draw rectangles and write instructions
            and score with turtle
        parameters:
            x: the abscissa of the location turtle should go to
            y: the ordinate of the location turtle should go to
            text: the text turtle will write within the rectangle
        return:
            a rectangle with specific size and color and text within it
            shown on the canvas
        '''
        turtle.goto(x, y)
        # set up the color of the pen
        turtle.color("white")
        # draw the rectangle
        self.draw_rectangle(135, 30, "#d2b48c")
        # go into the rectangle
        turtle.goto( x + 5, y + 3)
        # write the text
        turtle.write(text, font = ("Calibri", 13, "bold"))

    def display(self, number_dictionary, score, gameover, win):
        '''
        method: display
        purpose: this method is to clear the canvas and draw every element
            of the game 2048 with turtle, including an n * n board with
            respective numbers (non - zero), highlighted with different
            colors, score and the instructions of how to restart, end
            the game and how to move the cells.
        parameter:
            number_dictionary: a dictionary with n * n pairs of
                key and value - coordinate of the cell as key, number in
                the cell as value
            score: score the user obtained from each merge, integer
        return:
            1. display all the elements of the game with turtle, including
            the game board, numbers generated, instructions, scores.
            2. When the user reaches 2048 in any cell of the grid, message
            will be printed on the canvas and the game will be ended,
            ValueError will be raised.
            3. When there's no blank cell and shift cannot create blank
            space, message will be printed on the canvas and the game will
            be ended, ValueError will be raised.
        '''
        # clear the drawing by turtle
        turtle.clear()
        # set up the screen with specific screen size
        turtle.setup(width = self.screen_length, height = self.screen_height)
        # set up all the colors from 0 to 2048 as a dictionary
        colors = {0: "#d2b48c", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
                  16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850",
                  1024: "#edc53f", 2048: "#edc22e"}
        # set the turtle speed
        turtle.speed(0)
        # Hide the arrow of the turtle
        turtle.hideturtle()
        # Disable turtle animation
        turtle.tracer(0)
        turtle.penup()

        # display the score with helper function
        score = f"SCORE: {score}"
        self.instructions_and_score(-400, 270, score)

        # display the restart instruction with helper function
        restart = "RESTART: Press R"
        self.instructions_and_score(-400, 220, restart)

        # display the end instruction with helper function
        end = "END: Press E"
        self.instructions_and_score(-400, 170, end)

        # display the move instruction with helper function
        end = "MOVE: ← ↑ ↓ →"
        self.instructions_and_score(-400, 120, end)

        # get n * n turtle matrix and saved in a variable
        tiles = self.turtle_matrix()

        # if gameover, write message "GAME OVER" for 1 second, end the game
        # and raise ValueError
        if gameover:
            turtle.goto(-400, 30)
            turtle.color("red")
            turtle.write("GAME OVER!", font = ("Times New Roman", 17,
                                               "bold italic"))
            turtle.update()
            time.sleep(1)
            turtle.bye()
            # raise ValueError and print message on the IDLE as well to stop
            # the program
            raise ValueError("You lose the game!")

        # for loop to draw the game board and write down the respective values
        # per dictionary if the values are non-zero
        for key in number_dictionary.keys():
            # get the value of each key
            value = number_dictionary[key]
            # use the key of the dictionary to call the respective
            # turtle based on its coordinate
            my_turtle = tiles[key[1]][key[0]]
            # get the color for each cell based on the value of the cell
            color = colors.get(value)
            # draw the cell with specific color
            my_turtle.pendown()
            my_turtle.fillcolor(color)
            my_turtle.begin_fill()
            my_turtle.pensize(5)
            # for loop to iterate te process of drawing a cell
            for i in range(4):
                my_turtle.forward(self.distance)
                my_turtle.left(90)
            my_turtle.end_fill()
            my_turtle.penup()

            # write down the value of the cell if it's not zero
            if value != 0:
                my_turtle.goto((key[0] + 0.2) * self.distance - 200,
                               (key[1] + 0.3) * self.distance - 200)
                my_turtle.write(value, font=("Arial", 15, "normal"))

                #if the value reaches 2048, write respective message on the
                # canvas for 1 second and end the game, raise ValueError
                if win:
                    turtle.goto(-400, 60)
                    turtle.color("red")
                    turtle.write(f"You got 2048!", font = ("Times New "
                                                           "Roman", 17,
                                                            "bold italic"))
                    turtle.update()
                    time.sleep(1)
                    turtle.bye()
                    # raise ValueError printed to console, also to stop the
                    # program
                    raise ValueError("You win the game!")

        # update the above on the screen
        turtle.update()