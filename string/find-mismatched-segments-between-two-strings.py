class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        ans=[]
        n=len(s1)
        ns1=""
        ns2=""
        for i in range(n):
            if s1[i]!=s2[i]:
                ns1=ns1+s1[i]
                ns2=ns2+s2[i]
                #print(ns1,ns2)
                continue
            if ns1:
                ans.append([ns1,ns2])
                ns1=""
                ns2=""
        if ns1:
            ans.append([ns1,ns2])
        return ans
                