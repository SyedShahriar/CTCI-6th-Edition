class Solution(object):
    def OneAway(self,s1,s2):
        
        if s1==s2 : return True
        
        diff = abs(len(s1)-len(s2))
        
        if diff>1: return False
        
        if diff==0:
            counter =0
            for i in range(len(s1)):
                if s1[i]!=s2[i]: counter+=1
                if counter>1: return False
            return True
            
        else:
            
            if len(s1)>len(s2): longer,shorter = s1,s2
            else: longer,shorter (s2,s1)
            
            for i in range (len(shorter)):
                count = 0
                if shorter[i]!=longer[i+count]:
                    if count==1 or (shorter[i]!=longer[i+1]):
                        return False
                    count=1
        
        return True
        
        

if __name__ == "__main__":
    
    print(Solution().OneAway('cab','ad')) 