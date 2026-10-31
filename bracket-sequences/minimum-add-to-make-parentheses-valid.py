class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        n=len(s)
        ans=0
        for i in range(n):
            if s[i] == '(':
                st.append('(')
            else:
                if len(st)==0:
                    ans+=1
                else:
                    st.pop()
        return ans+len(st)