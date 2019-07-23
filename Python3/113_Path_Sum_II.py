# Time: O(n)
# Space: O(logn)
"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7   2   5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @return a list
    # 思路: 递归
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        if not root: return res

        def dfs(root: TreeNode, tmp: list, sum: int) -> None:
            if not root.left and not root.right:
                if root.val == sum:
                    res.append(tmp + [root.val])
            if root.left:
                dfs(root.left, tmp + [root.val], sum - root.val)
            if root.right:
                dfs(root.right, tmp + [root.val], sum - root.val)

        dfs(root, [], sum)
        return res


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    result = Solution().pathSum(root, 22)
    print(result)