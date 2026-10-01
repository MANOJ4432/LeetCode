class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        hm={}
        i=0
        n=len(nums)
        count=0
        while i < n-1:
            if nums[i] == nums[i+1]:
                count+=1
            elif (nums[i],nums[i+1]) in hm:
                hm[(nums[i],nums[i+1])]+=1
            elif (nums[i+1],nums[i]) in hm:
                 hm[(nums[i+1],nums[i])]+=1
            else:
                hm[(nums[i],nums[i+1])]=1
            i+=1
        maxi=0
        for key in hm:
            maxi=max(maxi,hm[key])
        return maxi+count
#if it is 2,3 or 3, 2 it belongs same pair ok 
# choose max freaquency pair 
#that is gonna be our answer
