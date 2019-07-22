# Time: O(n)
# Space: O(n)
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a TreeNode
    # 思路: 递归
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            mid=len(nums)//2
            tn=TreeNode(nums[mid])
            nums1=nums[0:mid]
            nums2=nums[mid+1:len(nums)]
            tn.left=self.sortedArrayToBST(nums1)
            tn.right=self.sortedArrayToBST(nums2)
        return tn

    def PrintFromTopToBottom(self, root):
        # print a TreeNode from top to bottom
        array = []
        result = []
        if root == None:
            return result

        array.append(root)
        while array:
            newNode = array.pop(0)
            result.append(newNode.val)
            if newNode.left != None:
                array.append(newNode.left)
            if newNode.right != None:
                array.append(newNode.right)
        return result


if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    result = Solution().sortedArrayToBST(nums)
    print(Solution().PrintFromTopToBottom(result))