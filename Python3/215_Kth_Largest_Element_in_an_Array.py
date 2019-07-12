"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the
kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
from typing import List


class Solution:
    # @return a integer
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        # 思路: 排序
        return sorted(nums)[-k]


class Solution_2:
    # @return a integer
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n)
        # Space: O(1)
        # 思路: 快排
        return self.quickSort(nums, 0, len(nums) - 1, k - 1)

    # 快排
    def quickSort(self, nums, lo, hi, k):
        if lo >= hi:
            return nums[lo]
        mid = self.partition(nums, lo, hi)
        if mid == k:
            return nums[mid]
        elif k < mid:
            return self.quickSort(nums, 0, mid - 1, k)
        else:
            return self.quickSort(nums, mid + 1, hi, k)

    # 切分
    def partition(self, a, lo, hi):
        pivot = a[lo]  # 选取第一个为枢轴值
        while lo < hi:
            while lo < hi and a[hi] <= pivot:
                hi -= 1
            a[lo] = a[hi]
            while lo < hi and a[lo] >= pivot:
                lo += 1
            a[hi] = a[lo]
        a[lo] = pivot
        return lo


if __name__ == '__main__':
    result = Solution().findKthLargest([3,2,1,5,6,4], 2)
    result_2 = Solution_2().findKthLargest([3,2,1,5,6,4], 2)
    print(result)
    print(result_2)