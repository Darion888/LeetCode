# Time: O(n)
# Space: O(n)
"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?

给定一个二叉树，返回它的 后序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

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
    # 思路: 迭代
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        cur=root
        res=[]
        backto=[]
        backto.append(None)
        while cur!=None:
            res.append(cur.val)
            if cur.left!=None:
                backto.append(cur.left)
            if cur.right!=None:
                cur=cur.right
            else:
                cur=backto.pop()
        res.reverse()
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = None
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution().postorderTraversal(root)
    print(result)