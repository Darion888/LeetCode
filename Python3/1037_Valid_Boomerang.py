# TIme: O(mn)
# Space: O(mn)
"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:
Input: [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: [[1,1],[2,2],[3,3]]
Output: false

Note:
·points.length == 3
·points[i].length == 2
·0 <= points[i][j] <= 100

回旋镖定义为一组三个点，这些点各不相同且不在一条直线上。

给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖。

示例 1：
输入：[[1,1],[2,3],[3,2]]
输出：true

示例 2：
输入：[[1,1],[2,2],[3,3]]
输出：false
 
提示：
·points.length == 3
·points[i].length == 2
·0 <= points[i][j] <= 100
"""
from typing import List


class Solution:
    # @return a boolean
    # 思路: 斜率

    def isBoomerang(self, points: List[List[int]]) -> bool:
        c=[]
        for i in range(2):
            b=[]
            for j in range(1):
                b.append(float((points[i][j]-points[i+1][j])))
                b.append(float(points[i][j+1]-points[i+1][j+1]))
                c.append(b)
        if c[0][1]*c[1][0]==c[1][1]*c[0][0]:
            flag=False
        else:
            flag=True
        return flag


if __name__ == "__main__":
    result = Solution().isBoomerang([[1,1],[2,2],[3,3]])
    print(result)