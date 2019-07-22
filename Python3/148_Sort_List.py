# Time: O(n)
# Space: O(n)
"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5

在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    # 思路: ListNode->List->ListNode
    def sortList(self, head: ListNode) -> ListNode:
        ha = self.ListNodeToList(head)
        return self.ListToListNode(ha)

    def ListNodeToList(self, head):
        if head == None:
            return
        stack = []
        first = ListNode(0)
        while head:
            stack.append(head.val)
            head = head.next
        stack = sorted(stack)
        return stack

    def ListToListNode(self, stack):
        first = ListNode(0)
        res = first
        while stack:
            first.next = ListNode(stack.pop(0))
            first = first.next
        return res.next


if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    result = Solution().sortList(head)
    print("{0} -> {1} -> {2} -> {3}".format(result.val, result.next.val, result.next.next.val, result.next.next.next.val))