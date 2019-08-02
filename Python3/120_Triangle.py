# Time: O(sum(N))
# Space: O(1)
# N: 三角形每一行宽度
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
·Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
·如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""
from typing import List


class Solution:
    # @return an integer
    # 思路: 动态回归
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
            triangle[i][-1] += triangle[i-1][-1]
        return min(triangle[-1])


if __name__ == "__main__":
    result = Solution().minimumTotal([
                                         [2],
                                        [3,4],
                                       [6,5,7],
                                      [4,1,8,3]
                                                ])
    print(result)