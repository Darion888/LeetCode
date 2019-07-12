# Time: O(n)
# Space: O(1)
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""
from typing import List


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #思路: 列表排序后比较第一项与最后一项
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        strs.sort()
        res = ''
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                res += x
            else:
                break
        return res


if __name__ == "__main__":
    result = Solution().longestCommonPrefix(["flower","flow","flight"])
    print(result)