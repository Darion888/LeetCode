# Time: O(n)
# Space: O(n)
"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = [0]
        for i in range(len(lists)):
            if lists[i] != None:
                res += Solution().ListNodeToList(lists[i])
        res.pop(0)
        if res != None:
            return Solution().ListToListNode(sorted(res))
        else:
            return

    def ListNodeToList(self, head):
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
    a = ListNode(1)
    a.next = ListNode(4)
    a.next.next = ListNode(5)
    b = ListNode(1)
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    c = ListNode(2)
    c.next = ListNode(6)
    lists = [a, b, c]
    result = Solution().mergeKLists(lists)
    print("{0} -> {1} -> {2} -> {3} -> {4} -> {5} -> {6} -> {7}".format(result.val, result.next.val, result.next.next.val,
                                                                        result.next.next.next.val, result.next.next.next.next.val,
                                                                        result.next.next.next.next.next.val,
                                                                        result.next.next.next.next.next.next.val,
                                                                        result.next.next.next.next.next.next.next.val))