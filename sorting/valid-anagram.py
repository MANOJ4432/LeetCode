class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        count=[0]*26
        for i in range(n):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1
        for i in range(26):
            if count[i]:
                return False
        return True