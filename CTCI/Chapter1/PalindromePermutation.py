class Solution(object):
    def PalindromePermutation(self,string):
        
        string = string.strip('').replace(' ','').lower()
        
        chars = {}
        
        for i in string:
            if i in chars.keys(): chars[i]+=1
            else: chars[i]=1
        
        isOdd = True
        tracker = 0
        
        if len(string)%2==0: isOdd=False
        
        for i in chars.keys():
            if chars[i]%2!=0:
                tracker+=1
        
        if tracker==0 and isOdd==False: return True
        elif tracker==1 and isOdd: return True
        
        else: return False
        

if __name__ == "__main__":
    
    print(Solution().PalindromePermutation('srace cras')) 