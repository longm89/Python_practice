"""
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        We check 2 cases:
            + when the palindrome has even length
                for each s[index] == s[index + 1], we go to two directions to
                check if we can extend the length of the palindrome
            + when the palindrome has odd length.
                for each s[index], we go to two directions to find
                the longest palindrome
        The time complexity is O(len(s)**2)
        The space complexity is O(1)
        There exists an O(len(s)) algorithm
        """

        max_string = ''

        # the even length case:
        for index in range(0, len(s) - 1):
            if s[index] == s[index + 1]:
                left = index
                right = index + 1
                while left > 0 and right < len(s)-1 and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                if len(max_string) < right - left + 1:
                    max_string = s[left:right+1]

        # the odd length case:
        for index in range(0, len(s)):
            left = index
            right = index
            while left > 0 and right < len(s)-1 and s[left - 1] == s[right+1]:
                left -= 1
                right += 1
            if len(max_string) < right - left + 1:
                max_string = s[left:right+1]

        return max_string
