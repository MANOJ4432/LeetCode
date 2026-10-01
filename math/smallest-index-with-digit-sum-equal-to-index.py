class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digitSum(num):
            ans=0
            while num!=0:
                ans+=num%10
                num=num//10
            return ans
        for i in range(len(nums)):
            if digitSum(nums[i]) == i:
                return i
        return -1