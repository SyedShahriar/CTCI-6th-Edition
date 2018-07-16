class Solution(object):
    def stringCompression(self,s):
        
        count =1
        string =[]
        for i in range(len(s)):
            if i>0:
                curr = s[i]
                prev = s[i-1]
                if curr==prev: 
                    count+=1 
                else: 
                    string.append(prev+str(count))
                    count =1
            if i==len(s)-1:
                string.append(curr+str(count)) 
                
        string = ''.join(string)
        
        if len(string)>len(s): return s
        else: return string
        
        

if __name__ == "__main__":
    
    print(Solution().stringCompression('aabccccca')) 