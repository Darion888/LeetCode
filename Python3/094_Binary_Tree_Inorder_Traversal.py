# Time: O(n)
# Space: O(n)
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

给定一个二叉树，返回它的 中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            res = []
            self.middle_digui(root, res)
        return res

    def middle_digui(self, root, res):
        if root == None:
            return
        self.middle_digui(root.left, res)
        res.append(root.val)
        self.middle_digui(root.right, res)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution().inorderTraversal(root)
    print(result)