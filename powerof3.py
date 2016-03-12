class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        max = 3 ** 32
        
        return (max % n) == 0