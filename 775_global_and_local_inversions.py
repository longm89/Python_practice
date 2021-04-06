"""
We have some permutation A of [0, 1, ..., N - 1], 
where N is the length of A.

The number of (global) inversions is the number 
of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i 
with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions 
is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
"""


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """
        The brute force solution is to count the number of 
        global inversions and local inversions. 
        The time complexity is O(len(A) ** 2) and space complexity
        is O(len(A) ** 2)
        
        We only need to check if at position current_pos, there exists
        a number bigger than it, at any position: 0, 1, 2, ..., current_pos - 2.
        If yes, we then return False
        If no, we then return True in the end.
        To do that, we could keep track of the maximum of all numbers from position
        0 to position current_pos - 2
        Edge cases: len(A) <= 2: return True
        
        """

        if len(A) <= 2:
            return True

        current_max = A[0]
        for current_pos in range(2, len(A)):
            if current_max > A[current_pos]:
                return False
            current_max = max(current_max, A[current_pos - 1])

        return True

