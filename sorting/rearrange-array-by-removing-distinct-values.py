class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[]
        count=n
        mini=float("inf")
        maxi=float("-inf")
        for i in range(n):
            mini=min(mini,nums[i])
            maxi=max(maxi,nums[i])
       
        size=maxi-mini+1
        countarr=[0]*size
       
        for i in range(n):
            countarr[nums[i]-mini]+=1
        print(countarr)
        while count!=0:
            for i in range(size):
                if countarr[i]!=0:
                    ans.append(i+mini)
                    countarr[i]-=1
                    count-=1
        return ans
                    
                    
        
        
       