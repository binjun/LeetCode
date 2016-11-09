# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        pos = 0
        maxlen = 0
        dic = {}
        for i in range(len(s)):
            print pos, s[i], i
            if s[i] in dic:
                maxlen = max(maxlen, dic[s[i]] - pos + 1)
                pos = dic[s[i]] + 1
            dic[s[i]] = i
            maxlen = max(maxlen, i - pos + 1)

        return maxlen

test =  Solution()

print "longestsubstring length is %d." % test.lengthOfLongestSubstring('dvdf')
