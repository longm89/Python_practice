"""
We are given two arrays A and B of words.  
Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, 
including multiplicity.  
For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  
You can return the words in any order.


Example 1:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Example 4:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        For each word in A, we will check if it's universal
        For each word in B, we only need to keep track of the multiplicty of
        each letter. Moreover, to check for the universality of A, we could
        combine all words in B together. In particular, we could keep a
        dictionary dict_B: dict_B[letter] = the maximum number of times
        a letter occurs in a word in B.
        To build the dictionary, it takes O(len(B) * len(word)).
        For each word in A, we count the multiplicty of each letter in word
        and we need that its multiplicty >= dict_B[letter]
        The time complexity is
        O(max(len(A) * 29 * len(word), len(B) * len(word)))
        """
        uni_words = []

        # build the B-dictionary
        dict_B = dict()
        for word in B:
            dict_word = dict()
            for letter in word:
                if letter in dict_word:
                    dict_word[letter] += 1
                else:
                    dict_word[letter] = 1
            for letter in dict_word:
                if letter in dict_B:
                    dict_B[letter] = max(dict_B[letter], dict_word[letter])
                else:
                    dict_B[letter] = dict_word[letter]
        # check each word in A
        for word in A:
            dict_word = dict()
            for letter in word:
                if letter in dict_word:
                    dict_word[letter] += 1
                else:
                    dict_word[letter] = 1
            universal = True
            for letter in dict_B:
                if letter not in dict_word or dict_word[letter] < dict_B[letter]:
                    universal = False
                    break
            if universal:
                uni_words.append(word)

        return uni_words
