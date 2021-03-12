"""
Given a string s, find the length of the longest substring without
repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not
a substring.
Example 4:

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a position start,
        the longest substring s[start], s[start + 1],..., s[stop] will
        be such that stop+1 == len(s) or s[stop + 1] in
        the current_set = {s[start], s[start+1],...,s[stop]}

        Hence, given a start position with a stop position,
        for start+1, the next_stop position will be farther away from
        the previous stop position, and such that next_stop+1 == len(s) or
        s[next_stop + 1] is in
        (current_set minus s[start]) union s[stop+1],...s[next_stop]
       
        We could use a Set to check if an element is in a Set, or to delete an
        element, the complexity for both operations is O(1)
        The time complexity is O(len(s))
        The space complexity is O(len(s))
        """

        if len(s) == 0:
            return 0

        # The first case when start = 0
        stop = 0
        current_set = {s[0]}
        while (stop+1 != len(s) and s[stop+1] not in current_set):
            stop += 1
            current_set.add(s[stop])
        max_length = len(current_set)

        # The case for start = 2,3,4,..., len(s) - 1
        for start in range(1, len(s)):
            next_stop = stop
            current_set.remove(s[start-1])
            while (next_stop+1 != len(s) and
                    s[next_stop+1] not in current_set):
                next_stop += 1
                current_set.add(s[next_stop])
            if max_length < next_stop-start+1:
                max_length = next_stop-start+1
            stop = next_stop
            
        return max_length
            