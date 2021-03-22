"""
Starting with a positive integer N, 
we reorder the digits in any order (including the original order) 
such that the leading digit is not zero.

Return true if and only if we can do this in a way such that 
the resulting number is a power of 2.

 

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
"""


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """
        We create a list of all numbers from 1 -> 2**30
        For each of these numbers, we convert them into string, then sort it
        in an order 0, 1, 2,..., 9
        For our number, we convert it to string, we then also sort it
        in an order of 0, 1, 2,..., 9
        we then go through the list to see if we could find the number
        """

        list_of_nums = ["".join(sorted(str(2**i))) for i in range(31)]
                     
        N_to_string = "".join(sorted(str(N)))

        return N_to_string in list_of_nums
