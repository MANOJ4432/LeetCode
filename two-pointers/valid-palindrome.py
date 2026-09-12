class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        s=s.lower()
        s1=""
        for i in range(n):
            if s[i].isalnum():
                s1+=s[i]
        print(s1)
        left=0
        right=len(s1)-1
        while left<right:
            if s1[left]!=s1[right]:
                return False
            left+=1
            right-=1

        return True