'''
Longest Palindrome

Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

'''


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return

        map_ = {}
        length = 0
        middle = False

        for item in s:
            if item in map_:
                map_[item] = map_.get(item) + 1
            else:
                map_[item] = 1
        for k, v in map_.items():
            if v % 2 != 0 and not middle:
                middle = True
                length += v
            elif v % 2 == 0:
                length += v
            elif middle:
                length += (v - 1)

        return length