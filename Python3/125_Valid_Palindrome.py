# Time: O(n)
# Space: O(1)
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""


class Solution:
    # @return a boolean
    def isPalindrome(self, s: str) -> bool:
        # 思路: 利用ASCII值比较, 留下小写字母和数字, 大写字母转换为小写字母
        s = list(filter(str.isalnum, s.lower()))
        return s == s[::-1]


if __name__ == "__main__":
    result = Solution().isPalindrome('A man, a plan, a canal: Panama')
    result_2 = Solution().isPalindrome("race a car")
    print(result)
    print(result_2)

