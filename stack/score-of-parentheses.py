class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        recent=""
        ans=0
        st=[]
        n=len(s)
        for i in range(n):
            if s[i] == '(':
                st.append(i)
                recent=i
            else:
                x=st.pop()
                if recent == x:
                    ans+=1<<len(st)
        return ans