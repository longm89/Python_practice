"""
You are given a binary string s. You are allowed to 
perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s 
and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., 
if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you 
need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, 
while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third 
and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""


class Solution:
    def minFlips(self, s: str) -> int:
        """
        for type-1 operation, we have
        s = s1 + s2 and a type-1 operation will produce s2 s1
        Given a last_cut_pos = len(s1)-1, and a choice of
        whether the first digit of the new string is 0 or 1,
        we need to calculate the number of flips (type-2)
        that we need to make to turn s2 s1 into alternating.
        We could calculate the number of flips above by:
        let num_flips[index][0] = num of flips to make
        s[index:] alternating assuming s[index] == "0"
        let num_flips[index][1] = num of flips to make
        s[index:] alternating assuming s[index] == "1"
        num_flips[index][0] = 0/1 + num_flips[index + 1][1]
        num_flips[index][1] = 0/1 + num_flips[index + 1][0]

        """
        num_flips = [[0, 0] for index in range(len(s) + 1)]
        if s[-1] == "0":
            num_flips[len(s) - 1][1] = 1
        else:
            num_flips[len(s) - 1][0] = 1
        for index in range(len(s) - 2, -1, -1):
            for digit in range(2):
                num_flips[index][digit] = num_flips[index + 1][1 - digit]
            if s[index] == "0":
                num_flips[index][1] += 1
            else:
                num_flips[index][0] += 1
        min_flips = len(s)

        for last_cut_pos in range(len(s)):
            for first_digit in range(2):
                num_of_s2_flips = num_flips[last_cut_pos + 1][first_digit]
                len_of_s2 = len(s) - last_cut_pos - 1
                first_digit_s1 = (first_digit + len_of_s2) % 2
                digit_after_s1 = (first_digit_s1 + last_cut_pos + 1) % 2
                num_of_s1_flips = (
                    num_flips[0][first_digit_s1]
                    - num_flips[last_cut_pos + 1][digit_after_s1]
                )
                min_flips = min(min_flips, num_of_s2_flips + num_of_s1_flips)

        return min_flips
