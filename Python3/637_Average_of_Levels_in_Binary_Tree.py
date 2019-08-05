# Time: O(N^2)
# Space: O(N)
"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:
The range of node's value is in the range of 32-bit signed integer.

给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:
输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].

注意：
节点值的范围在32位有符号整数范围内。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a List[float]
    # 思路: 层次遍历

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = [root]
        target = []
        while ans:
            n = len(ans)
            tmp,sum_= [],0
            for i in range(n):
                r =ans.pop(0)
                sum_+=r.val
                if r.left:
                    ans.append(r.left)
                if r.right:
                    ans.append(r.right)
            target.append(sum_/(i+1))
        return target


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().averageOfLevels(root)
    print(result)