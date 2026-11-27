class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n=len(nums)
        i,j=0,0
        zero=0
        ans=0
        while j < n:
            if nums[j] == 0:
                zero+=1
            if zero > k:
                if nums[i] == 0:
                    zero-=1
                i+=1
            if zero <= k:
                ans=max(ans,j-i+1)
            j+=1
        return ans