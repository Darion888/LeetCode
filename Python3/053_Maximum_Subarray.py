# Time: O(n)
# Space: O(1)

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle.

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
from typing import List


class Solution:
    # @return an integer
    #思路: 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)

if __name__ == '__main__':
    result = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(result)