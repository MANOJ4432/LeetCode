class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        actual_sum=n*(n+1)/2
        sum_value=0
        for i in range(n):
            sum_value+=nums[i]
        return int(actual_sum-sum_value)