
class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        l=lower
        h=lower
        result=[]
        lasthit=-1
        while l <= upper and h <=upper:
            if BS(nums,h):
                if l!=h:
                    lasthit=h
                    lis=[l,h-1]
                    result.append(lis)
                    l=h+1
                else:
                    lasthit=h
                    l+=1
            h+=1
        if lasthit!=upper:
            lis=[l,h-1]
            result.append(lis)
        return result
def BS(arr,key):
    l=0
    h=len(arr)-1
    while l <= h:
        mid=(l+h)//2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            h=mid-1
        else:
            l=mid+1
    return False
    
        
                
                
        