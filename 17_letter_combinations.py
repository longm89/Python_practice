"""
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.



Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

"""


class Solution:
    def letterCombinations(self, digits: str):
        """
        We keep a dict of letters dict_letters for the conversion of
        digits to letters:
        dict_letters ={'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqs', '8':'tuv', '9': 'wxyz'}

        We could use recursion:

        Let possibleCombination(digits) be the list of possible combinations
        of letters, given a string digits.

        if len(digits) == 0:
            return []

        if len(digits) == 1:
                return [letter for letter in dict_letters[digits[0]]]

        result = []
        for output in possibleCombination(digits[1:]):
            for letter in dict_letters[digits[0]]:
                result.append(letter + output)
        Time complexity: O(4**len(digits))
        Space complexity: O(len(digits)), without counting the space for the array result
        """

        dict_letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def possibleCombinations(digits):

            if len(digits) == 0:
                return []

            if len(digits) == 1:
                return [letter for letter in dict_letters[digits[0]]]

            result = []

            for output in possibleCombinations(digits[1:]):
                for letter in dict_letters[digits[0]]:
                    result.append(letter + output)

            return result

        return possibleCombinations(digits)

