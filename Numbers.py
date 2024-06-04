'''
CS5001
2023Spring
Project: 2048 - Numbers
Yun Lu
This program is to generate, update and return number dictionary, which
consists of n * n items, with coordinate as keys and number as value.
Example:
    1. initialize the dictionary with 4 * 4 keys and 0 as their values
    2. randomly pick two or three keys and assign them with value 2 or 4
    3. update the dictionary when the user shifts all the numbers to left
        / right / up / down
    4. merge the cells with the same value (no other number in between)in the
        same row / column and placed to the left cell for direction "left",
        similar logic for direction "right", "up" and "down"
    5. update the score with the merged value
    6. if there are keys with value zero, randomly pick a key with value 0
        and assign it with value 2 or 4, otherwise, gameover = True. If
        there's a key with value 2048, win = True
'''

import random
import turtle
import time

class Numbers():
    '''
    class: Numbers
    This class is to generate, update and return number dictionary,
    which consists of n * n items, coordinates as keys and numbers as values.
    Also initialize and update the score which comes from the merged numbers.
    If there's no 0 in the values of the dict, gameover = true, and if
    there's 2048 in the values, win = True
    '''
    def __init__(self, size):
        '''
        Constructor: generate attribute for the object
        parameter: size of the game board
        return: none
        '''
        # generate the size attribute of the object
        self.size = size
        # generate the score of the object
        self.score = 0
        # generate the attribute of game over,initialize to False
        self.gameover = False
        # generate the attribute of win，initialize to False
        self.win = False

    def random_pair_generator(self, number_of_pairs):
        '''
        method: random_pair_generator
        purpose: helper method to randomly generate specific number of
            different pairs of numbers, ranging from 0 to (size -1)， which
            denotes the coordinate of each cell
        parameter:
            number_of_pairs: how many number of different pairs is needed,
            integer
        return:
            list of tuples, each tuple containing the coordinate of the cell
            in the game board
        '''
        # initialize an empty list
        pairs = []
        i = 1
        # while loop to iterate the process of generating different pairs
        # until reaching the number of pairs required
        while i <= number_of_pairs:
            # the value in the tuple should within the size - 1
            a = random.randint(0, self.size - 1)
            b = random.randint(0, self.size - 1)
            # avoid duplicated tuples
            if (a, b) not in pairs:
                pairs.append((a, b))
                i += 1
            else:
                i += 0
        return pairs

    def coordinate_matrix(self):
        '''
        method: coordinate_matrix
        purpose: helper method to generate a nested list, consisting of
            coordinates as elements in list
        parameter: none
        return: n * n number of coordinates[j, i] in a list, both j and i
            are within the range of size (not included)
        '''
        # initialize an empty list
        coordinate_matrix = []
        # for loop to iterate the process of appending the coordinate [j, i],
        # both j and i are within the range of size (not included)
        for i in range(self.size):
            for j in range(self.size):
                coordinate_matrix.append([j, i])
        return coordinate_matrix

    def initialize_number_dictionary(self):
        '''
        method: initialize_number_dictionary
        purpose: this method is to generate original number dictionary,
            with the coordinates as keys, and 0 as their respective values
        parameter: none
        return: a dictionary with n * n items, keys are the coordinates,
            values are all 0, meanwhile randomly pick two or more keys
            and assign them with number 2 or 4
        '''
        # reset the score to 0 when this method is called
        self.score = 0
        # generate number matrix in dictionary
        coordinate_matrix = self.coordinate_matrix()
        # create an empty dictionary
        number_dictionary = dict()
        # for loop to assign value to all the keys
        for element in coordinate_matrix:
            # convert keys (coordinates) into tuples to make coordinates
            # immutable
            key = tuple(element)
            # assign each key with value 0
            number_dictionary[key] = 0

        # randomly generate 2 or 3 coordinates to be initialized with value 2
        # or 4
        number_of_keys = random.randint(2, 3)
        # generate coordinates and store in a variable as a list
        pair_list = self.random_pair_generator(number_of_keys)
        for element in pair_list:
            # assign the keys with 2 or 4 for element
            number_dictionary[element] = random.choice([2, 4])
        # return the updated dictionary
        return number_dictionary

    def keys_nested_list(self, number_dictionary, direction):
        '''
        method: keys_nested_list
        purpose: helper method to create a nested list of keys for
            different directions
        parameter:
            number_dictionary: dictionary with  n * n items
            direction: move direction - left, right, up, down in string
        return:
            a nested list of keys
        '''
        # initialize an empty list
        keys_nested_list = []
        # for loop to iterate the process of appending sublist
        for i in range(self.size):
            # initialize the sublist as empty list
            keys_sublist = []
           # for loop to append keys in the same row / column to the sublist
            for key in number_dictionary.keys():
                # append the keys in the same row when move horizontally
                if key[1] == i and (
                        direction == "left" or direction == "right"):
                    keys_sublist.append(key)
                # append the keys in the same column when move vertically
                elif key[0] == i and (
                        direction == "down" or direction == "up"):
                    keys_sublist.append(key)
            # if move right or up, reverse the list
            if direction == "right" or direction == "up":
                keys_sublist = keys_sublist[::-1]
            # append the list (row, column)
            keys_nested_list.append(keys_sublist)
        return keys_nested_list

    def move_numbers(self, keys_nested_list, number_dictionary):
        '''
        method: move_numbers
        purpose: helper method to move the numbers by updating the
        values of the number dictionary
        parameters:
            keys_nested_list: nested list of keys of the dictionary
            number_dictionary: dictionary with coordinate as keys, numbers
            as values
        return:
            updated number_dictionary
        '''
        # initialize an empty list
        value_nested_list = []
        # for loop to examine each row / column of keys
        for each in keys_nested_list:
            # initialize an empty sublist
            value_sublist = []
            # for loop to examine each value of each key
            for index in range(self.size):
                value = number_dictionary[each[index]]
                # if the respective value is not 0 then append to the new
                # sublist
                if value != 0:
                    value_sublist.append(value)
            # fill each sublist with 0 until its length reaches the size
            for i in range(self.size - len(value_sublist)):
                value_sublist.append(0)
            # return the updated nested list of values
            value_nested_list.append(value_sublist)

        # re-assign the value to each key and return the updated dictionary
        for m in range(self.size):
            for n in range(self.size):
                number_dictionary[keys_nested_list[m][n]] = \
                    value_nested_list[m][n]
        return number_dictionary

    def shift_processor(self, number_dictionary, direction):
        '''
        method: shift_processor
        purpose: this method is to process the action of shifting numbers
        parameter:
            number_dictionary: dictionary with  n * n items, coordinate as
                keys and number as respective value
            direction: move direction - left, right, up, down in string
        return: updated number dictionary
        '''
        # nested list of keys based on the direction and current dictionary
        keys_nested_list = self.keys_nested_list(number_dictionary, direction)
        # move all cells to the specific direction before merge and update
        # the dictionary
        number_dictionary = self.move_numbers(keys_nested_list,
                                           number_dictionary)

        # iterate the merge process for each row of the nested list
        for each in keys_nested_list:
            # for each row / column, check each coordinate, except for the
            # last element
            for j in range(self.size - 1):
                #  tell if the current element has the same value with the
                #  next one
                if number_dictionary[each[j]] == number_dictionary[each[j +
                                                                        1]]:
                    # double the current value
                    number_dictionary[each[j]] *= 2
                    # increase the score by the sum of merged value
                    self.score += number_dictionary[each[j]]
                    # set the next element to 0
                    number_dictionary[each[j + 1]] = 0

        # move all the numbers to the direction post merge and update the dict
        number_dictionary = self.move_numbers(keys_nested_list,
                                              number_dictionary)
        return number_dictionary

    def dictionary_postshift(self, number_dictionary):
        '''
        method: dictionary_postshift
        purpose: this method is to update the number dictionary post shift,
            by assigning random key (with value 0) with value 2 or 4,
            also update the boolean for self.win and self.gameover
        parameter: number dictionary
        return: updated number_dictionary if the game is not over or 2048
        is not achieved, otherwise gameover = True or win = True
        '''
        # initiate empty list
        blank_cells_left = []
        # check the value of each key
        for key in number_dictionary.keys():
            value = number_dictionary[key]
            # collect all the cells with value 0 and append to the list
            if value == 0:
                blank_cells_left.append(key)
            # win = Ture when any of the key has value 2048
            elif value == 2048:
                self.win = True

        # gameover = True if there's no 0 in the value
        if len(blank_cells_left) == 0:
            self.gameover = True

        else:
            # randomly pick one of the key with value 0
            position = random.randint(0, len(blank_cells_left) - 1)
            # assign value 2 or 4 to that key
            number_dictionary[blank_cells_left[position]] = \
                random.choice([2, 4])
            # return the updated dictionary
            return number_dictionary