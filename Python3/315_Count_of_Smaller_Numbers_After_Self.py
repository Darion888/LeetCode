# Time: O(n^2)
# Space: O(n)
"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where
counts[i] is the number of smaller elements to the right of nums[i].

Example:
Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。

示例:

输入: [5,2,6,1]
输出: [2,1,1,0]
解释:
5 的右侧有 2 个更小的元素 (2 和 1).
2 的右侧仅有 1 个更小的元素 (1).
6 的右侧有 1 个更小的元素 (1).
1 的右侧有 0 个更小的元素.
"""
from typing import List


class Solution:
    # @return a List[int]
    # 思路: 二分查找
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans=[]
        tmp = []
        for i in reversed(nums):
            pos = self.bisect(tmp, i)
            ans.append(pos)
            tmp.insert(pos, i)
        return list(reversed(ans))

    def bisect(self, a, x):
        left = 0
        right = len(a)
        while left < right:
            mid = (left + right) // 2
            if a[mid] < x:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    result = Solution().countSmaller([5,2,6,1])
    print(result)