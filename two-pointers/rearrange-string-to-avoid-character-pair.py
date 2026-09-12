class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        new_s=""
        n=len(s)
        for i in range(n):
            if s[i]==y:
                new_s+=y
        #print(new_s)
        for j in range(n):
            if s[j]==x:
                new_s+=x
        #print(new_s)
        for i in range(n):
            if s[i]!=x and s[i]!=y:
                new_s+=s[i]
        return new_s