class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        left,bottom=n-1,0
        while(left>=0 and bottom<m):
            if target==matrix[bottom][left]:
                    return True
            elif target>matrix[bottom][left]:
                bottom+=1
            else:
                left-=1
        return False