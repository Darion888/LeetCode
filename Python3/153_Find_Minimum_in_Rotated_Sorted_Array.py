"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0

假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
请找出其中最小的元素。
你可以假设数组中不存在重复元素。

示例 1:
输入: [3,4,5,1,2]
输出: 1

示例 2:
输入: [4,5,6,7,0,1,2]
输出: 0
"""
from typing import List


class Solution:
    # @return a integer
    def findMin(self, nums: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(1)
        # 思路: 排序后输出0号元素
        return sorted(nums)[0]


class Solution_2:
    # @return a integer
    def findMin(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        # 思路: 直接输出数列最小值
        return min(nums)


class Solution_3:
    # @return a integer
    def findMin(self, nums: List[int]) -> int:
        # Time: O(logn)
        # Space: O(1)
        # 思路: 二分搜索
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = int(left + (right - left) / 2)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == "__main__":
    result = Solution().findMin([3,4,5,1,2])
    result_2 = Solution_2().findMin([3,4,5,1,2])
    result_3 = Solution_3().findMin([3,4,5,1,2])
    print(result)
    print(result_2)
    print(result_3)
