class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lp=[1]*n
        rp=[1]*n
        for i in range(1,n):
            lp[i]=(lp[i-1]*nums[i-1])
        for i in range(n-2,-1,-1):
            rp[i]=(rp[i+1]*nums[i+1])
        new_nums=[0]*n
        for i in range(n):
            new_nums[i]=(lp[i]*rp[i])
        return new_nums