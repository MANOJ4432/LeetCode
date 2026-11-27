class Solution:
    def checkString(self, s: str) -> bool:
        l=0
        while l < len(s) and s[l]!= 'b':
            l+=1
        while l < len(s):
            if s[l] == 'a':
                return False
            l+=1
        return True