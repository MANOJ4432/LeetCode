from collections import deque
class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        s1,s2=0,0
        q=deque()
        n=len(nums)
        for i in range(n):
            if i < n//2:
                s1+=nums[i]
            else:
                s2+=nums[i]
            q.append(nums[i])
        count=0
        if s1 > s2 :
            count+=1
        for _ in range(n-1):
            s2=s2-q[n//2]+q[0]
            s1=s1-q[0]+q[n//2]
            x=q.popleft()
            q.append(x)
            if s1 > s2:
                count+=1
        return count
            
            
            
        
        