class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total=0
        n=len(nums)
        for i in range(n):
            total+=nums[i]
        key=total-x
        best=-1
        left=0
        window_sum=0
        for right in range(n):
            window_sum+=nums[right]
            while window_sum > key and left <= right:
                window_sum-=nums[left]
                left+=1
            if window_sum == key:
                best=max(best,right-left+1) 
        return n-best if best!=-1 else -1
        


