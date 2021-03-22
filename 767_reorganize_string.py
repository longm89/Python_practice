"""
Given a string S, check if the letters can be rearranged so that 
two characters that are adjacent to each other are not the same.

If possible, output any possible result.  
If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

"""


class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        The result depends only on the frequency of the letters
        Let freq[letter] = the number of times the letter appears
        Each time, we will choose a letter with the highest frequency, 
        different from the previously chosen one
        to put in the end of the result 
        The time complexity is O(len(s)**2)
        """

        freq_dict = {}
        result = ""
        for letter in S:
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1
        prev_letter = None

        for i in range(len(S)):
            max_freq = -1
            chosen_letter = None
            for letter in freq_dict:
                if letter != prev_letter:
                    if max_freq < freq_dict[letter]:
                        max_freq = freq_dict[letter]
                        chosen_letter = letter
            if chosen_letter:
                result += chosen_letter
                freq_dict[chosen_letter] -= 1
                if freq_dict[chosen_letter] == 0:
                    freq_dict.pop(chosen_letter)
                prev_letter = chosen_letter
            else:
                return ""

        return result

