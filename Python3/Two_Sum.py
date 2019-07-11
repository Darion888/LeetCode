# Time: O(n)
# Space: O(n)

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

给定一个整型数组 nums 和一个目标值 target ，请找出数组中和为 target 的两个整数，并返回这两个数的数组下标。
假设：
1）每个输入只对应一个答案；
2）不允许重复使用数组中的数值。
"""
from typing import List


class Solution:
    # @return a List[int]
    def twoSum(self, nums: List[int], target: int):
        map = {}
        for i, num in enumerate(nums):
            if target - num in map:
                return [map[target - num], i]
            else:
                map[num] = i


if __name__ == '__main__':
    result = Solution().twoSum([2, 7, 11, 15], 9)
    print(result)
