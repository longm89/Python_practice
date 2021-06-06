"""
Given two n x n binary matrices mat and target, 
return true if it is possible to make mat equal to target by 
rotating mat in 90-degree increments, or false otherwise.
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make 
mat equal target.
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by 
rotating mat.
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], 
target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times 
to make mat equal target.

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.

"""


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        """
        Given a matrix, after turning 90 degree,
        the last column becomes the last row, with the order reverse
        In general, the i-th column becomes the i-th row, 
        with the order reverse
        rot_mat[i][j] = mat[n-1-j][i]
        Try to rotate the mat and then check if it's target.
        """
        n = len(mat)
        current_mat = [[mat[row][col] for col in range(n)] for row in range(n)]
        for num_of_rot in range(4):
            rot_mat = [[None for col in range(n)] for row in range(n)]
            for i in range(n):
                for j in range(n):
                    rot_mat[i][j] = current_mat[n - 1 - j][i]
            is_rotation = True
            for i in range(n):
                for j in range(n):
                    if rot_mat[i][j] != target[i][j]:
                        is_rotation = False
                        break
                if not is_rotation:
                    break
            if is_rotation:
                return True
            current_mat = rot_mat
        return False
