"""
Given an m x n 2D binary grid grid which represents
a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        for each unvisited '1', we use DFS to visit all the '1' nearby
        We then count the number of islands
        """

        num_of_islands = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def DFS(row, col):
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row and new_row < len(grid):
                    if 0 <= new_col and new_col < len(grid[0]):
                        if grid[new_row][new_col] == "1":
                            grid[new_row][new_col] = "v"
                            DFS(new_row, new_col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    grid[row][col] = 'v'
                    num_of_islands += 1
                    DFS(row, col)

        return num_of_islands

