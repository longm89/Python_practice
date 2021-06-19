"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, 
where words[i] is a non-empty string, 
and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal 
using any number of operations, and false otherwise.

 

Example 1:

Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.
Example 2:

Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """
        we need that the total number of times each character
        appears in all the words divisible by the number of words
        we make a dictionary total_freq and go through
        all the words to count the number of times each character appears.
        The time complexity is O(max(len(words) * len(words[i])))
        The space complexity is O(len(words))
        """

        total_freq = {}
        num_of_words = len(words)
        for word in words:
            for letter in word:
                if letter not in total_freq:
                    total_freq[letter] = 1
                else:
                    total_freq[letter] += 1

        for letter in total_freq:
            if total_freq[letter] % num_of_words != 0:
                return False

        return True

        """
        tests:
        ["abc", "aabc", "bc"] 
        total_freq["a"] = 3, total_freq["b"] = 3, total_freq[c] = 3 => True
        ["ab", "a"] => False
        ["aaaaaa"] => True
        """
