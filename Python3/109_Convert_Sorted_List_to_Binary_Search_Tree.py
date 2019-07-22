# Time: O(n)
# Space: O(n)
"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every
node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @return a treenode
    # 思路: ListNode->Array->TreeNode
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = Solution().ListNodeToList(head)
        return Solution().sortedArrayToBST(nums)

    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        else:
            mid = len(nums) // 2
            tn = TreeNode(nums[mid])
            nums1 = nums[0:mid]
            nums2 = nums[mid + 1:len(nums)]
            tn.left = self.sortedArrayToBST(nums1)
            tn.right = self.sortedArrayToBST(nums2)
        return tn

    def ListNodeToList(self, head):
        if head == None:
            return
        stack = []
        first = ListNode(0)
        while head:
            stack.append(head.val)
            head = head.next
        return stack

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
    head = ListNode(-10)
    head.next = ListNode(-3)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(9)
    result = Solution().sortedListToBST(head)
    print(Solution().PrintFromTopToBottom(result))