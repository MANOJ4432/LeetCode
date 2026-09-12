class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        new_s=""
        s1=""
        s2=""
        n=len(s)
        l,h=0,n-1
        while l<h:
            x=min(s[l],s[h])
            s1+=x
            s2=x+s2
            l+=1
            h-=1
        if l==h:
            return s1+s[l]+s2
        return s1+s2

        