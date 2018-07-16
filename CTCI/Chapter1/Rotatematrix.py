class Solution(object):
    #  def rotate_matrix(self,m):
    #   n = len(m)
    #   rotm = [None] * n
    #   for row in xrange(n):
    #     rotm[row] = [None] * n
    #   for row in xrange(n):
    #     for col in xrange(n):
    #       rotm[n - col - 1][row] = m[row][col]
    #   return rotm
      
    def rotate_matrix_in_place(self,m):
          
        n = len(m)
          
        for row in range(n):
            for col in range(row,n):
                temp = m [col][row]
                print temp
                m[col][row]= m[row][col]
                m[row][col]=temp
        
        print m
        
        for row in range(n):
            index = n-1
            col =0
            while col<index:
                temp = m[row][col]
                m[row][col]=m[row][index]
                m[row][index]=temp
                index-=1
                col+=1
                #m[row]=list(reversed(m[row]))
            
            
        
        
        return m
        

if __name__ == "__main__":
    mat3 = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().rotate_matrix_in_place(mat3)) 