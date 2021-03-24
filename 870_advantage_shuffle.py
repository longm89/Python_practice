"""
Given two arrays A and B of equal size, 
the advantage of A with respect to B is the number 
of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its 
advantage with respect to B.


Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        """
        We remark that the advantage of A with B doesn't depend on the order
        of elements in B. To find this max advantage, we could sort B first.
        After that, for each element of B, from smallest to biggest, we find
        the smallest element of A such that it's bigger than this element and so on.
        The rest of A, we put to the end.
        To recover the index, we keep a list sorted_B whose element is
        of the form (num, index) and sort using num
        We then sort A and try to put elements of A into result_for_sorted_B.
        Our final result will be a list result, such that: for i in range(len(B)):
        result[sorted_B[i][1]] = A_for_sorted_B[i]

        The time complexity is O(N logN)
        The space complexity is O(N)
        """

        sorted_B = [(B[index], index) for index in range(len(B))]
        sorted_B.sort(key=lambda element: element[0])
        sorted_A = sorted(A)
        result_for_sorted_B = []
        result = [0 for i in range(len(A))]
        rest_A = []

        last_A = -1
        for i in range(len(sorted_B)):
            last_A += 1
            while last_A < len(A):
                if sorted_B[i][0] >= sorted_A[last_A]:
                    rest_A.append(sorted_A[last_A])
                    last_A += 1
                else:
                    result_for_sorted_B.append(sorted_A[last_A])
                    break

        for num in rest_A:
            result_for_sorted_B.append(num)

        for i in range(len(A)):
            result[sorted_B[i][1]] = result_for_sorted_B[i]

        return result
