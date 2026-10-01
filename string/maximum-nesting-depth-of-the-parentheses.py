class Solution:
    def maxDepth(self, s: str) -> int:
        cnt=0
        ans=0
        n=len(s)
        for i in range(n):
            if s[i]=='(':
                cnt+=1
                ans=max(ans,cnt)
            elif s[i]==')':
                cnt-=1
        return ans


            