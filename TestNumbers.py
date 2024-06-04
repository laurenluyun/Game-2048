'''
CS5001
2023Spring
Project: 2048 - TestNumbers
Yun Lu
This program is to test the class Numbers - the methods (not helper
functions) within the class.
'''
import unittest
from Numbers import Numbers

class TestNumbers(unittest.TestCase):
    '''
    class: TestNumbers
    This class is to test the main methods (not helper functions) of class
    Numbers
    '''
    def setUp(self) -> None:
        '''
        method: setUp
        purpose: set up attributes and variables that are needed for the tests
        '''
        self.size = 4
        self.score = 0
        self.my_numbers = Numbers(self.size)

    def test_constructor(self):
        '''
        method: test_constructor
        purpose: this method is to test constructor of class Numbers
        parameter: none
        return: pass the test if expected = actual result, fail otherwise
        '''
        self.assertEqual(4, self.size)
        self.assertEqual(0, self.score)

    def test_initialize_number_dictionary(self):
        '''
        method: test_initialize_number_dictionary
        purpose: this method is to test initialize_number_dictionary
        parameter: none
        return: pass the test if expected = actual result, fail otherwise
        '''
        # generate a dictionary by calling the method
        dictionary_actual = self.my_numbers.initialize_number_dictionary()
        keys_expected = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1),
                         (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2),
                         (0, 3), (1, 3), (2, 3), (3, 3)]

        # generate a list of all the keys of the dict
        keys_actual = []
        for key in dictionary_actual.keys():
            keys_actual.append(key)

        # check the dictionary has the correct keys
        self.assertEqual(keys_expected, keys_actual)

        # check all the values are 2 or 4 or 0
        for value in dictionary_actual.values():
            self.assertTrue(value == 2 or value == 4 or value == 0)

        # check the number of keys with value 2 or 4 is either 2 or 3
        count = 0
        for value in dictionary_actual.values():
            if value in [2, 4]:
                count += 1
        self.assertIn(count, [2, 3])

    def test_shift_processor(self):
        '''
        method: test_shift_processor
        purpose: this method is to test shift_processor
        parameter: none
        return: pass the test if expected = actual result, fail otherwise
        '''
        # check left-shifting case where there's no merge
        dict_1 = {(0, 0): 2, (1, 0): 0, (2, 0): 0, (3, 0): 0,
                  (0, 1): 2, (1, 1): 0, (2, 1): 0, (3, 1): 4,
                  (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                  (0, 3): 0, (1, 3): 4, (2, 3): 0, (3, 3): 0}
        dict_1_expected = {(0, 0): 2, (1, 0): 0, (2, 0): 0, (3, 0): 0,
                           (0, 1): 2, (1, 1): 4, (2, 1): 0, (3, 1): 0,
                           (0, 2): 2, (1, 2): 0, (2, 2): 0, (3, 2): 0,
                           (0, 3): 4, (1, 3): 0, (2, 3): 0, (3, 3): 0}
        self.assertEqual(dict_1_expected,
                         self.my_numbers.shift_processor(dict_1, "left"))
        # check the score is updated
        self.assertEqual(0, self.my_numbers.score)

        # check left-shifting case where two same number next to each other
        # merged, and two same numbers not next to each other merged
        dict_2 = {(0, 0): 4, (1, 0): 0, (2, 0): 0, (3, 0): 4,
                  (0, 1): 2, (1, 1): 2, (2, 1): 0, (3, 1): 0,
                  (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                  (0, 3): 0, (1, 3): 4, (2, 3): 0, (3, 3): 0}
        dict_2_expected = {(0, 0): 8, (1, 0): 0, (2, 0): 0, (3, 0): 0,
                           (0, 1): 4, (1, 1): 0, (2, 1): 0, (3, 1): 0,
                           (0, 2): 2, (1, 2): 0, (2, 2): 0, (3, 2): 0,
                           (0, 3): 4, (1, 3): 0, (2, 3): 0, (3, 3): 0}
        self.assertEqual(dict_2_expected,
                         self.my_numbers.shift_processor(dict_2, "left"))
        # check the score is updated
        self.assertEqual(12, self.my_numbers.score)

        # check left-shifting case where there are three and four same
        # numbers in the same row
        dict_3 = {(0, 0): 2, (1, 0): 2, (2, 0): 2, (3, 0): 4,
                  (0, 1): 2, (1, 1): 0, (2, 1): 2, (3, 1): 2,
                  (0, 2): 2, (1, 2): 2, (2, 2): 2, (3, 2): 2,
                  (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 0}
        dict_3_expected = {(0, 0): 4, (1, 0): 2, (2, 0): 4, (3, 0): 0,
                           (0, 1): 4, (1, 1): 2, (2, 1): 0, (3, 1): 0,
                           (0, 2): 4, (1, 2): 4, (2, 2): 0, (3, 2): 0,
                           (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 0}
        self.assertEqual(dict_3_expected,
                         self.my_numbers.shift_processor(dict_3, "left"))
        # check the score is updated
        self.assertEqual(28, self.my_numbers.score)

        # check right-shifting case where there's no merge
        dict_4 = {(0, 0): 2, (1, 0): 0, (2, 0): 0, (3, 0): 0,
                  (0, 1): 2, (1, 1): 0, (2, 1): 0, (3, 1): 4,
                  (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                  (0, 3): 2, (1, 3): 4, (2, 3): 0, (3, 3): 0}
        dict_4_expected = {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 2,
                           (0, 1): 0, (1, 1): 0, (2, 1): 2, (3, 1): 4,
                           (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                           (0, 3): 0, (1, 3): 0, (2, 3): 2, (3, 3): 4}
        self.assertEqual(dict_4_expected,
                         self.my_numbers.shift_processor(dict_4, "right"))
        # check the score is updated
        self.assertEqual(28, self.my_numbers.score)

        # check right-shifting case where two same number next to each other
        # merged, and two same numbers not next to each other merged
        dict_5 = {(0, 0): 4, (1, 0): 0, (2, 0): 0, (3, 0): 4,
                  (0, 1): 2, (1, 1): 2, (2, 1): 0, (3, 1): 0,
                  (0, 2): 4, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                  (0, 3): 2, (1, 3): 4, (2, 3): 0, (3, 3): 0}
        dict_5_expected = {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 8,
                           (0, 1): 0, (1, 1): 0, (2, 1): 0, (3, 1): 4,
                           (0, 2): 0, (1, 2): 0, (2, 2): 4, (3, 2): 2,
                           (0, 3): 0, (1, 3): 0, (2, 3): 2, (3, 3): 4}
        self.assertEqual(dict_5_expected,
                         self.my_numbers.shift_processor(dict_5, "right"))
        # check the score is updated
        self.assertEqual(40, self.my_numbers.score)

        # check right-shifting case where there are three and four same
        # numbers in the same row
        dict_6 = {(0, 0): 2, (1, 0): 2, (2, 0): 2, (3, 0): 4,
                  (0, 1): 2, (1, 1): 0, (2, 1): 2, (3, 1): 2,
                  (0, 2): 2, (1, 2): 2, (2, 2): 2, (3, 2): 2,
                  (0, 3): 2, (1, 3): 4, (2, 3): 8, (3, 3): 16}
        dict_6_expected = {(0, 0): 0, (1, 0): 2, (2, 0): 4, (3, 0): 4,
                           (0, 1): 0, (1, 1): 0, (2, 1): 2, (3, 1): 4,
                           (0, 2): 0, (1, 2): 0, (2, 2): 4, (3, 2): 4,
                           (0, 3): 2, (1, 3): 4, (2, 3): 8, (3, 3): 16}
        self.assertEqual(dict_6_expected,
                         self.my_numbers.shift_processor(dict_6, "right"))
        # check the score is updated
        self.assertEqual(56, self.my_numbers.score)

        # check down-shifting case where there's no merge
        dict_7 = {(0, 0): 0, (1, 0): 0, (2, 0): 2, (3, 0): 2,
                  (0, 1): 0, (1, 1): 2, (2, 1): 0, (3, 1): 4,
                  (0, 2): 0, (1, 2): 0, (2, 2): 4, (3, 2): 2,
                  (0, 3): 2, (1, 3): 4, (2, 3): 0, (3, 3): 4}
        dict_7_expected = {(0, 0): 2, (1, 0): 2, (2, 0): 2, (3, 0): 2,
                           (0, 1): 0, (1, 1): 4, (2, 1): 4, (3, 1): 4,
                           (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                           (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 4}
        self.assertEqual(dict_7_expected,
                         self.my_numbers.shift_processor(dict_7, "down"))
        # check the score is updated
        self.assertEqual(56, self.my_numbers.score)

        # check down-shifting case where two same number next to each other
        # merged, and two same numbers not next to each other merged
        dict_8 = {(0, 0): 0, (1, 0): 2, (2, 0): 0, (3, 0): 4,
                  (0, 1): 0, (1, 1): 0, (2, 1): 0, (3, 1): 0,
                  (0, 2): 2, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                  (0, 3): 2, (1, 3): 2, (2, 3): 4, (3, 3): 0}
        dict_8_expected = {(0, 0): 4, (1, 0): 4, (2, 0): 4, (3, 0): 4,
                           (0, 1): 0, (1, 1): 0, (2, 1): 0, (3, 1): 2,
                           (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 0,
                           (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 0}
        self.assertEqual(dict_8_expected,
                         self.my_numbers.shift_processor(dict_8, "down"))
        # check the score is updated
        self.assertEqual(64, self.my_numbers.score)

        # check down-shifting case where there are three and four same
        # numbers in the same row
        dict_9 = {(0, 0): 2, (1, 0): 2, (2, 0): 2, (3, 0): 4,
                  (0, 1): 2, (1, 1): 2, (2, 1): 2, (3, 1): 2,
                  (0, 2): 2, (1, 2): 2, (2, 2): 2, (3, 2): 2,
                  (0, 3): 2, (1, 3): 4, (2, 3): 8, (3, 3): 16}
        dict_9_expected = {(0, 0): 4, (1, 0): 4, (2, 0): 4, (3, 0): 4,
                           (0, 1): 4, (1, 1): 2, (2, 1): 2, (3, 1): 4,
                           (0, 2): 0, (1, 2): 4, (2, 2): 8, (3, 2): 16,
                           (0, 3): 0, (1, 3): 0, (2, 3): 0, (3, 3): 0}
        self.assertEqual(dict_9_expected,
                         self.my_numbers.shift_processor(dict_9, "down"))
        # check the score is updated
        self.assertEqual(84, self.my_numbers.score)

        # check up-shifting case where there's no merge
        dict_10 = {(0, 0): 2, (1, 0): 0, (2, 0): 2, (3, 0): 2,
                  (0, 1): 0, (1, 1): 2, (2, 1): 0, (3, 1): 4,
                  (0, 2): 0, (1, 2): 0, (2, 2): 4, (3, 2): 2,
                  (0, 3): 0, (1, 3): 4, (2, 3): 0, (3, 3): 4}
        dict_10_expected = {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 2,
                           (0, 1): 0, (1, 1): 0, (2, 1): 0, (3, 1): 4,
                           (0, 2): 0, (1, 2): 2, (2, 2): 2, (3, 2): 2,
                           (0, 3): 2, (1, 3): 4, (2, 3): 4, (3, 3): 4}
        self.assertEqual(dict_10_expected,
                         self.my_numbers.shift_processor(dict_10, "up"))
        # check the score is updated
        self.assertEqual(84, self.my_numbers.score)

        # check up-shifting case where two same number next to each other
        # merged, and two same numbers not next to each other merged
        dict_11 = {(0, 0): 2, (1, 0): 2, (2, 0): 4, (3, 0): 4,
                  (0, 1): 2, (1, 1): 0, (2, 1): 0, (3, 1): 0,
                  (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 2,
                  (0, 3): 0, (1, 3): 2, (2, 3): 0, (3, 3): 0}
        dict_11_expected = {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0,
                           (0, 1): 0, (1, 1): 0, (2, 1): 0, (3, 1): 0,
                           (0, 2): 0, (1, 2): 0, (2, 2): 0, (3, 2): 4,
                           (0, 3): 4, (1, 3): 4, (2, 3): 4, (3, 3): 2}
        self.assertEqual(dict_11_expected,
                         self.my_numbers.shift_processor(dict_11, "up"))
        # check the score is updated
        self.assertEqual(92, self.my_numbers.score)

        # check up-shifting case where there are three and four same
        # numbers in the same row
        dict_12 = {(0, 0): 2, (1, 0): 2, (2, 0): 2, (3, 0): 4,
                  (0, 1): 2, (1, 1): 2, (2, 1): 2, (3, 1): 2,
                  (0, 2): 2, (1, 2): 2, (2, 2): 2, (3, 2): 2,
                  (0, 3): 2, (1, 3): 4, (2, 3): 8, (3, 3): 16}
        dict_12_expected = {(0, 0): 0, (1, 0): 0, (2, 0): 0, (3, 0): 0,
                           (0, 1): 0, (1, 1): 2, (2, 1): 2, (3, 1): 4,
                           (0, 2): 4, (1, 2): 4, (2, 2): 4, (3, 2): 4,
                           (0, 3): 4, (1, 3): 4, (2, 3): 8, (3, 3): 16}
        self.assertEqual(dict_12_expected,
                         self.my_numbers.shift_processor(dict_12, "up"))
        # check the score is updated
        self.assertEqual(112, self.my_numbers.score)

    def test_dictionary_postshift(self):
        '''
        method: test_dictionary_postshift
        purpose: this method is to test dictionary_postshift
        parameter: none
        return: pass the test if expected = actual result, fail otherwise
        '''

        dictionary_1 = {(0, 0): 0}
        new_dictionary_1 = self.my_numbers.dictionary_postshift(dictionary_1)
        # check the new dictionary still has length of 1 and the value of
        # that key has been assigned with either 2 or 4
        self.assertEqual(len(new_dictionary_1), 1)
        self.assertIn(new_dictionary_1[(0, 0)], [2, 4])

        # check gameover = True when all the cells are occupied
        dictionary_2 = {(0, 0): 2, (1, 0): 4, (0, 1): 8, (1, 1): 16}
        self.my_numbers.dictionary_postshift(dictionary_2)
        self.assertEqual(True, self.my_numbers.gameover)

        # check win = True when there is 2048 in a cell
        dictionary_4 = {(0, 0): 2048, (1, 0): 4, (0, 1): 8, (1, 1): 16}
        self.my_numbers.dictionary_postshift(dictionary_4)
        self.assertEqual(True, self.my_numbers.win)

        dictionary_3 = {(0, 0): 0, (1, 0): 2, (0, 1): 0, (1, 1): 0}
        # check the method can assign 2 or 4 to keys with value zero in a
        # for loop
        for i in range(3):
            new_dictionary_3 = self.my_numbers.dictionary_postshift(
                dictionary_3)
            # length of the dictionary is not changed
            self.assertEqual(len(new_dictionary_3), 4)
            # number of non-zero values is added by 1
            self.assertEqual(sum(value != 0 for value in
                                 new_dictionary_3.values()), i + 2)

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()