class Solution:
    def removeOuterParentheses(self, s: str) -> str:
    
        ans=""
        n=len(s)
        len_valid=0
        for i in range(n):
            if s[i] == '(':
                if len_valid!=0:
                    ans+=s[i]
                len_valid+=1
            else:
                len_valid-=1
                if len_valid!=0:
                    ans+=s[i]
        return ans
                
