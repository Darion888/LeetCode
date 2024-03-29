# Time: O(N)
# Space: O(N)
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:
s = "leetcode"
返回 0.
s = "loveleetcode",
返回 2.

注意事项：您可以假定该字符串只包含小写字母。
"""


class Solution:
    # @return an integer
    # 思路: 字典+集合
    def firstUniqChar(self, s: str) -> int:
        dic = {c: s.count(c) for c in set(s)}

        for i, c in enumerate(s):
            if dic[c] == 1:
                return i

        return -1


if __name__ == "__main__":
    result = Solution().firstUniqChar(s = "leetcode")
    print(result)