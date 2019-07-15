# Time: O(n)
# Space: O(n)
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明: 1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @return a ListNode
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 思路: 所有链表压入一个列表里，然后反转相应的位置。创建新的链表
        if head ==None:
            return
        if m ==n:
            return head
        stack = []
        first = ListNode(0)
        while head:
            stack.append(head.val)
            head = head.next
        stack[m-1:n] = reversed(stack[m-1:n])
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
    result = Solution().reverseBetween(head, 2, 4)
    print("{0} -> {1} -> {2} -> {3} -> {4}".format(result.val, result.next.val, result.next.next.val, result.next.next.next.val,  result.next.next.next.next.val))
