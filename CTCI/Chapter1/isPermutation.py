class Solution(object):
    def isPermutation(self,str1, str2):
      counter = dict()
      
      for letter in str1:
        if letter in counter.keys(): counter[letter] += 1
        else: counter[letter] = 1
        
      for letter in str2:
        if not letter in counter:
          return False
        counter[letter] -= 1
        if counter[letter] == 0:
          del counter[letter]
      return len(counter) == 0



if __name__ == "__main__":
    print(Solution().isPermutation('keca','cake')) 