"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:
输入: [10,2]
输出: 210

示例 2:
输入: [3,30,34,5,9]
输出: 9534330

说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""
from typing import List


class Solution:
    # @return a string
    def largestNumber(self, nums: List[int]) -> str:
        # Time: O(n^2)
        # Space: O(1)
        # 思路: 冒泡排序
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) - int(str(nums[j]) + str(nums[i])) < 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        nums=[str(i) for i in nums]
        if int(''.join(nums)) == 0:
            return '0'
        else:
            return ''.join(nums)


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution_2:
    # @return a string
    def largestNumber(self, nums: List[int]) -> str:
        # Time: O(nlgn)
        # Space: O(n)
        # 思路: 自定义排序
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == "__main__":
    result = Solution().largestNumber([3,30,34,5,9])
    result_2 = Solution_2().largestNumber([3,30,34,5,9])
    print(result)
    print(result_2)