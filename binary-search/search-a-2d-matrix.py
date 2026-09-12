def floorBS(arr,target,m):
    idx=-1
    l,h=0,m-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid][0]<=target:
            idx=mid
            l=mid+1
        else:
            h=mid-1
    return idx
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row=floorBS(matrix,target,m)
        if row==-1:
            return False
        l,h=0,n-1
        while(l<=h):
            mid=(l+h)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                h=mid-1
            else:
                l=mid+1
        return False
