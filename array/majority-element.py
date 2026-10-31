class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hm={}
        n=len(nums)
        if n == 1:
            return nums[0]
        for i in range(n):
            if nums[i] not in hm:
                hm[nums[i]]=1
            else:
                hm[nums[i]]+=1
                if hm[nums[i]] > n//2:
                    return nums[i]
        
        