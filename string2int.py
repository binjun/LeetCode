# -*- coding: utf-8 -*-
"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.
If you want a challenge, please do not see below and ask yourself what are the possible input cases.
"""
import unittest

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0

        inputchars = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9};
        inputval = []
        signs = {"+":1,"-":-1}
        useless = [" "]
        count = 0
        result = 0
        sign = 1

        for c in str:
            if c in useless:
                count += 1
            else:
                break

        firstchar = str[count]

        if firstchar in signs:
            sign = signs[firstchar]
            count += 1
        elif firstchar not in inputchars:
            return 0
        else:
            pass

        for c in str[count:]:
            if c in inputchars:
                result = result * 10 + inputchars[c]
            else:
                break

        result = result * sign
        if result > 2147483647:
            result = 2147483647
        if result < -2147483648:
            result = -2147483648
        return result

myTest = Solution()

class myUnitest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcase1(self):
        self.assertEqual(myTest.myAtoi("123456"), 123456)

    def testcase2(self):
        self.assertEqual(myTest.myAtoi("-123456"), -123456)

    def testcase3(self):
        self.assertEqual(myTest.myAtoi("1234a"), 1234)

    def testcase4(self):
        self.assertEqual(myTest.myAtoi("+1"), 1)

    def testcase5(self):
        self.assertEqual(myTest.myAtoi(""), 0)

    def testcase6(self):
        self.assertEqual(myTest.myAtoi("0123"), 123)

    def testcase7(self):
        self.assertEqual(myTest.myAtoi("    123"), 123)

    def testcase8(self):
        self.assertEqual(myTest.myAtoi("     +1234"), 1234)

    def testcase9(self):
        self.assertEqual(myTest.myAtoi("     -1234"), -1234)

    def testcase10(self):
        self.assertEqual(myTest.myAtoi("    -0012a34"), -12)

    def testcase11(self):
        self.assertEqual(myTest.myAtoi("-2147483649"), -2147483648)

    def testcase11(self):
        self.assertEqual(myTest.myAtoi("2147483649"), 2147483647)

unittest.main()
