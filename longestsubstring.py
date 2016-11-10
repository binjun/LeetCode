# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
import unittest

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
            #print pos, s[i], i, maxlen
            if s[i] in dic:
                pos = max(pos, dic[s[i]]+ 1)
                maxlen = max(maxlen, i - pos + 1)
            else:
                maxlen += 1
                
            dic[s[i]] = i

        return maxlen

test =  Solution()

class mytest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcase1(self):
        self.assertEqual(test.lengthOfLongestSubstring('abcab'), 3)

    def testcase2(self):
        self.assertEqual(test.lengthOfLongestSubstring('a'), 1)

    def testcase3(self):
        self.assertEqual(test.lengthOfLongestSubstring('abb'), 2)

    def testcase4(self):
        self.assertEqual(test.lengthOfLongestSubstring('abcdefcef'), 6)

    def testcase5(self):
        self.assertEqual(test.lengthOfLongestSubstring('abab'), 2)

    def testcase6(self):
        self.assertEqual(test.lengthOfLongestSubstring('abcb'), 3)


unittest.main()
