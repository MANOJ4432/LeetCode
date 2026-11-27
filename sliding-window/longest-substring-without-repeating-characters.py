class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs=set()
        n=len(s)
        i=0
        j=0
        ans=0
        while j < n:
            if s[j] not in hs:
                hs.add(s[j])
                j+=1
                continue
            ans=max(ans,len(hs))
            while s[i]!=s[j]:
                hs.remove(s[i])
                i+=1
            j+=1
            i+=1
        ans=max(ans,len(hs))
        return ans
