class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n=len(nums)
        x=str(x)
        count=0
        for i in range(n):
            sum=0
            for j in range(i,n):
                sum+=nums[j]
                temp_str=str(sum)
                if temp_str[0]==x and temp_str[-1]==x:
                    count+=1
        return count