"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n/2⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
"""
from typing import List


class Solution:
    # @return an integer
    # Time: O(nlgn)
    # Space: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        # 思路：排序后取中位数
        nums.sort()
        return nums[len(nums) // 2]


class Solution_2:
    # @return an integer
    # Time: O(n)
    # Space: O(1)
    def majorityElement(self, nums):
        # 思路：Boyer-Moore 投票算法
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == '__main__':
    result = Solution().majorityElement([3, 2, 3])
    print(result)
    result_2 = Solution_2().majorityElement([2, 2, 1, 1, 1, 2, 2])
    print(result_2)
