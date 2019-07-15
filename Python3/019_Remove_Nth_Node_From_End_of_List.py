# Time: O(n)
# Space: O(n)
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 思路: 所有链表压入一个列表里，然后删除相应的位置。创建新的链表
        if head ==None:
            return
        stack = []
        first = ListNode(0)
        while head:
            stack.append(head.val)
            head = head.next
        stack.pop(-n)
        res = first
        while stack:
            first.next = ListNode(stack.pop(0))
            first = first.next
        return res.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    result = Solution().removeNthFromEnd(head, 2)
    print("{0} -> {1} -> {2} -> {3}".format(result.val, result.next.val, result.next.next.val, result.next.next.next.val))
