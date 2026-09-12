class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm={}
        n=len(s)
        i=0
        j=0
        ans=0
        while i < n:
            if s[i] in hm:
                ans=max(ans,len(hm))
                x=hm[s[i]]
                while j <= x:
                    hm.pop(s[j])
                    j+=1   
            hm[s[i]]=i
            i+=1
        ans=max(ans,len(hm))
        return ans