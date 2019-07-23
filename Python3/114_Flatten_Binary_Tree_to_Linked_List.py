# Time: O(n)
# Space: O(logn)
"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

给定一个二叉树，原地将它展开为链表。

例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @return none
    # 思路:  迭代
    def flatten(self, root: TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right: p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
        return root


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = Solution().flatten(root)
    print(result.val)
    print(result.right.val)
    print(result.right.right.val)
    print(result.right.right.right.val)
    print(result.right.right.right.right.val)
    print(result.right.right.right.right.right.val)