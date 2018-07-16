class Solution(object):
    def URLify(self,string,truelength):
        
        
        spaces=0
        
        for i in range(truelength):
            if string[i] ==" ":
                spaces +=1
                
        index = spaces*2 + truelength
        
        output = ['-']*index
        
        for i in range(truelength-1,-1,-1):
            if string[i]==" ":
                output[index-1]="0"
                output[index-2]="2"
                output[index-3] ="%"
                index -=3
            else:
                output[index-1]=string[i]
                index-=1
            
        return ''.join(output)

if __name__ == "__main__":
    
    print(Solution().URLify("Mr John Smith    ",13)) 