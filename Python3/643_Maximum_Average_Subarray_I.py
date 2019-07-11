# Time: O(n)
# Space: O(1)
"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value.
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

注意:
1 <= k <= n <= 30,000。
所给数据范围 [-10,000，10,000]。
"""
from typing import List


class Solution:
    # @return a float
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #思路:滑动窗口
        maxsum = sum(nums[:k])
        res = maxsum
        for i in range(len(nums)-k):
            maxsum = maxsum - nums[i] + nums[i+k]
            res = max(res, maxsum)
        return res/k


if __name__ == "__main__":
    result = Solution().findMaxAverage([1,12,-5,-6,50,3], 4)
    print(result)