import time
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount <= 0:
            return 0
            
        count = len(coins)  
        if count <= 0:
            return -1
            
        self.minChanges = 2 ** 31
        coins.sort()
        self.coins = coins[::-1]
        self.changes = [0] * count
        
        def find(remain, coins, level):
            if level == count - 1 or remain == 0:
                num = remain / coins[level]
                rest = remain - coins[level] * num
                if rest == 0:
                    self.changes[level] = num
                    total = sum(self.changes[:level + 1])
                    #print self.changes
                    if total < self.minChanges:
                        #print "update\n"
                        self.minChanges = total
            else:
                for x in range(remain / coins[level], -1, -1):
                    self.changes[level] = x
                    tmp = remain - coins[level] * x
                    #if tmp >= coins[level + 1]:
                    find(tmp, coins, level + 1)
                        
        find(amount, self.coins, 0)
        
        if self.minChanges == 2 ** 31:
            return -1
        else:
            return self.minChanges
                        
coinSolution = Solution()
time.clock()
result = coinSolution.coinChange([277,196,194,358,263,257], 7477)    
print "duration of function is %s\n" % time.clock() 
print result 
raw_input()      