# Time: O(n)
# Space: O(n)
"""
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None: return
        ha = self.ListNodeToList(head)
        while val in ha:
            ha.remove(val)
        return self.ListToListNode(ha)

    def ListNodeToList(self, head):
        # 所有链表压入一个列表里
        if head == None:
            return
        stack = []
        first = ListNode(0)
        while head:
            stack.append(head.val)
            head = head.next
        return stack

    def ListToListNode(self, stack):
        first = ListNode(0)
        res = first
        while stack:
            first.next = ListNode(stack.pop(0))
            first = first.next
        return res.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    result = Solution().removeElements(head, 6)
    print("{0} -> {1} -> {2} -> {3} -> {4}".format(result.val, result.next.val, result.next.next.val, result.next.next.next.val, result.next.next.next.next.val))