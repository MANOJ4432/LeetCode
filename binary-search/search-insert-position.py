class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        l,u=0,n-1
        mid=int()
        while(l<=u):
            mid=(l+u)//2
            if(target>nums[mid]):
                l=mid+1
            elif(target<nums[mid]):
                u=mid-1
            else:
                return mid
        return l
      