# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret_dict = {}
        for idx in range(len(nums)):
            if nums[idx] in ret_dict:
                return [ret_dict[nums[idx]], idx]
            else:
                ret_dict[target - nums[idx]] = idx
        else:
            return []
