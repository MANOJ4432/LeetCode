def digitrange(num):
    s=str(num)
    min_digit=-1
    key=False
    for i in range(10):
        for j in range(len(s)):
            if s[j]==str(i):
                min_digit=i
                key=True
                break
        if key:
            break
    max_digit=10
    key=False
    for i in range(9,-1,-1):
        for j in range(len(s)):
            if s[j]==str(i):
                max_digit=i
                key=True
                break
        if key:
            break
    return max_digit-min_digit
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        max_range=-1
        digit_range=[0]*len(nums)
        for i in range(len(nums)):
            digit_range[i]=digitrange(nums[i])
            if digit_range[i] > max_range:
                max_range=digit_range[i]
        #print(digit_range)
        sum=0
        for i in range(len(nums)):
            if digit_range[i]==max_range:
                sum+=nums[i]
        return sum
     
            
        