class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        m=len(requests)
        sum=requests[0]
        for i in range(1,m):
            sum+=abs(requests[i]-requests[i-1])
        return sum