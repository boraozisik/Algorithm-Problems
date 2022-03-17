"""
You are given an array representing a grid of a 2-dimensional map,along with the dimensions to correctly parse it.
Array only consist of 1's and 0's , where 1 represents land and 0 represents seas.
An island is a collection of vertically or horizontally connected lands.Find the largest island.

Constraints:

length of island map is equal to width x height
width > 0  height > 0

"""


class Solution:

   def calculate(self, matrix):
      self.row_len = len(matrix)
      self.column_len = len(matrix[0])
      max_island = 0
      for row in range(self.row_len):
         for column in range(self.column_len):
            if matrix[row][column] == 1:
               self.total = 0
               self.dfs(matrix, row, column)
               max_island = max(max_island, self.total)
      return max_island

   def dfs(self, matrix, row, column):
      self.total += 1
      matrix[row][column] = 0
      if row - 1 >= 0 and matrix[row - 1][column] == 1:
         self.dfs(matrix, row - 1, column)
      if column - 1 >= 0 and matrix[row][column - 1] == 1:
         self.dfs(matrix, row, column - 1)
      if row + 1 < self.row_len and matrix[row + 1][column] == 1:
         self.dfs(matrix, row + 1, column)
      if column + 1 < self.column_len and matrix[row][column + 1] == 1:
         self.dfs(matrix, row, column + 1)


solution = Solution()
matrix = [[1, 1, 0, 1, 1], [0, 0, 1, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1]]
print(solution.calculate(matrix))