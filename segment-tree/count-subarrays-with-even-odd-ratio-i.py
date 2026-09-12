class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            x,y=0,0
            for j in range(i,n):
                if nums[j]&1:
                    y+=1
                else:
                    x+=1
                if y!=0:
                    if x/y <= a/b:
                        ans+=1
        return ans
                    
                    