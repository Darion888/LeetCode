# Time: O(m*n)
# Space: O(1)
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
·Integers in each row are sorted from left to right.
·The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
·每行中的整数从左到右按升序排列。
·每行的第一个整数大于前一行的最后一个整数。

示例 1:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true

示例 2:
输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""
from typing import List


class Solution:
    # @return a boolean
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 思路: 逐行查找
        for i in matrix:
            if target in i:
                return True
        return False


if __name__ == "__main__":
    result = Solution().searchMatrix([
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], target = 3)
    print(result)