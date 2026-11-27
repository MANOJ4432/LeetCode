class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        l=n-k
        r=n-1
        sum_value=0
        ans=0
        for i in range(l,r+1):
            sum_value+=cardPoints[i]
        if k == n:
            return sum_value
        ans=max(ans,sum_value)
        sum_value-=cardPoints[l]
        l=(l+1)%n
        r=(r+1)%n
        sum_value+=cardPoints[r]
        while r < k:
            ans=max(ans,sum_value)
            sum_value-=cardPoints[l]
            l=(l+1)%n
            r=(r+1)%n
            sum_value+=cardPoints[r]
        return ans
