class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        ans=0
        span_green=max(lights)
        n=len(arrivalTime)
        for i in range(n):
            r=arrivalTime[i]%period
            if r >= span_green:
                ans=max(ans,period-r)
        return ans
                
                