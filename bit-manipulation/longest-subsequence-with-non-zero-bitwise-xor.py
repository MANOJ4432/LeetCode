class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                break
        else:
            return 0
        for i in range(n):
            xor=xor^nums[i]
        
        if xor!=0:
            return n
        else:
            return n-1