def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        n=len(nums)
        ans=float("-inf")
        for i in range(n-1):
            for j in range(i+1,n):
                g=gcd(nums[i],nums[j])
                strength=(nums[i]*nums[j])//(g*g)
                ans=max(ans,strength)
        return ans
                
        
        
        