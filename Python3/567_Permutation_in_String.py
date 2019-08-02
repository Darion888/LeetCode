# Time: O(N)
# Space: O(N)
"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
·The input strings only contain lower case letters.
·The length of both given strings is in range [1, 10,000].

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").

示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False

注意：
·输入的字符串只包含小写字母
·两个字符串的长度都在 [1, 10,000] 之间
"""


class Solution:
    # @return a boolean
    # 思路: 滑动窗口
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1.__len__() > s2.__len__():
            return False
        if s1 == '':
            return True

        import collections
        s1_dic = collections.Counter(s1)
        s2_dic = collections.Counter(s2[0:s1.__len__() - 1 + 1])

        sli_dic = {}
        for key in s1_dic.keys():
            if key in s2_dic.keys():
                sli_dic[key] = s2_dic[key]
            else:
                sli_dic[key] = 0

        if sli_dic == s1_dic:
            return True

        for i in range(s1.__len__(), s2.__len__()):
            if s2[i - s1.__len__()] in s1_dic.keys():
                sli_dic[s2[i - s1.__len__()]] -= 1
            if s2[i] in s1_dic.keys():
                sli_dic[s2[i]] += 1
            if sli_dic == s1_dic:
                return True
        return False


if __name__ == "__main__":
    result = Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo")
    print(result)