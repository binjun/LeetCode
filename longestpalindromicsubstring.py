# -*- coding: utf-8 -*-
"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example2:
Input: "cbbd"
Output: "bb"
"""
import unittest

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""

        length = len(s)
        if length <= 1:
            return ret

        for i in range(length, 1, -1):
            for j in range(length - i + 1):
                substring = s[j:i+j]
                #print "substring = %s" % substring
                if substring == substring[::-1]:
                    ret = substring
                    break
            else:
                continue
            break

        return ret

solution = Solution()

class myUnittest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcase1(self):
        self.assertEqual(solution.longestPalindrome("babad"), "bab")

    def testcase2(self):
        self.assertEqual(solution.longestPalindrome("cbbd"), "bb")

unittest.main()
