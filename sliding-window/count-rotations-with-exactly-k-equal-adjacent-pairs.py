from collections import deque
def checker(arr):
    score=0
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            score+=1
    return score
        
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        q=deque()
        n=len(s)
        for i in range(n):
            q.append(s[i])
        ans=0
        for _ in range(n):
            score=checker(q)
            if score == k:
                ans+=1
            x=q.popleft()
            q.append(x)
        return ans