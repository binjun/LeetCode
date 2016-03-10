class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ascii = "abcdefghijklmnopqrstuvwxyz"
        list_count = [s.count(c) for c in ascii]
        list_visited = [0 for c in ascii]
        list_solution = []
        start = chr('a')
        
        for c in s:
            pos = chr(c) - start
            list_count[pos]--
            
            if list_visited[pos] > 0:
                #c is alread in solution list
                continue
                
            if list_solution
            
        