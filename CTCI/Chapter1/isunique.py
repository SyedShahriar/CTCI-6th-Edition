class Solution(object):
    #letters a-z
    def isUnique(self,s): 
        
        checker = 0
        
        for i in s:
            val = ord(i) - ord('a')
            if (checker & (1<<val))>0:
                return False
            checker = checker | (1<<val)
        return True


if __name__ == "__main__":
    print(Solution().isUnique('joking')) 