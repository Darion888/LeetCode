# Time: O(|S|+|T|)
# Space: O(|S|+|T|)
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
·If there is no such window in S that covers all characters in T, return the empty string "".
·If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"

说明：
·如果 S 中不存这样的子串，则返回空字符串 ""。
·如果 S 中存在这样的子串，我们保证它是唯一的答案。
"""


class Solution:
    # @return a string
    # 思路: 滑动窗口
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        from collections import Counter

        dict_t = Counter(t)

        required = len(dict_t)

        l, r = 0, 0

        formed = 0

        window_counts = {}

        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


if __name__ == "__main__":
    result = Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
    print(result)