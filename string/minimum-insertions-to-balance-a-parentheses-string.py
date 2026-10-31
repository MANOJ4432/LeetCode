class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        open=0
        ans=0
        i=0
        while i < n:
            if s[i] == '(':
                open+=1
                i+=1
            else:
                if open == 0 :
                    if i+1 < n and s[i+1] == ')':
                        ans+=1
                        i+=2
                    else:
                        ans+=2
                        i+=1
                else:
                    open-=1
                    if i+1 < n and s[i+1] ==')':
                        i+=2
                    else:
                        ans+=1
                        i+=1

        return ans+open*2