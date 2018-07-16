class Solution(object):

    def zeromatrix(self,matrix):
        m = len(matrix)
        
        if m==0: return matrix
        
        n = len(matrix[0])
        
        zero_rows = []
        zero_cols = []
        
        for i in range (m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        
        for x in zero_rows:
            for y in range(n):
                matrix[x][y]=0
        
        for x in zero_cols:
            for y in range(m):
                matrix[y][x]=0
        
        return matrix
                    
                    
        


if __name__ == "__main__":
    mat3 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
    print(Solution().zeromatrix(mat3)) 