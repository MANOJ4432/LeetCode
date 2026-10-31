def validPar(y):
            st=[]
            for x in y:
                if x == '(':
                    st.append(x)
                elif x == ')':
                    if len(st) == 0:
                        return False
                    st.pop()
            return len(st)==0
        
def func(s,idx,req,tans,fans,n):
    if idx >= n and req != 0:
        return 
    if req == 0:
        if validPar(tans):

            fans.append(tans)
        return 
    if s[idx] == '(' or s[idx] == ')':
                func(s,idx+1,req-1,tans+s[idx],fans,n)
                func(s,idx+1,req,tans,fans,n)
    else:
                func(s,idx+1,req-1,tans+s[idx],fans,n)
    return 
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def checkMinInvalidPar():
            opened=0
            closed=0
            for x in s:
                if x=='(':
                    opened+=1
                elif x==')':
                    if opened > 0:
                        opened-=1
                    else:
                        closed+=1
            return opened+closed
        extra_par=checkMinInvalidPar()
        n=len(s)
        required=n-extra_par
        fans=[]
        func(s,0,required,"",fans,n)
        return list(set(fans))
