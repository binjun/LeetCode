class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) <= 0:
            return ""
            
        ascii = "abcdefghijklmnopqrstuvwxyz"
        list_count = [s.count(c) for c in ascii]
        list_visited = [0] * 26
        list_solution = []
        start = ord('a')
        list_solution.append(s[0])
        list_count[ord(s[0]) - start] -= 1
        list_visited[ord(s[0]) - start] = 1
        
        for c in s[1:]:
            value = ord(c)
            pos = value - start
            list_count[pos] -= 1
            
            if list_visited[pos] > 0:
                #c is alread in solution list
                continue
            
            print c
            print list_solution
            for x in range(len(list_solution)):
                if list_solution[-1] > c:
                    index = ord(list_solution[-1]) - start
                    if list_count[index] > 0:
                        list_solution.pop()
                        list_visited[index] = 0
                else:
                    break
                    
            list_solution.append(c)
            list_visited[pos] = 1
            
            print list_solution
            
        return "".join(list_solution)
            
                
            
way = Solution()  

#print way.removeDuplicateLetters("bcabc")

print way.removeDuplicateLetters("cbacdcbc")

raw_input()          
        