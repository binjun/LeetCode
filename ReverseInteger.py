# -*- coding: utf-8 -*-
"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
import unittest

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0

        if x < 0:
            result = -int(str(-x)[::-1])
        else:
            result = int(str(x)[::-1])

        if (result > 2147483647) or (result < -2147483648):
            return 0
            
        return result

test = Solution()
class myuinttest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcase1(self):
        self.assertEqual(test.reverse(123), 321)

    def testcase2(self):
        self.assertEqual(test.reverse(-123), -321)

unittest.main()
