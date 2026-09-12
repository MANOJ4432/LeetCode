class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str=strs[0]
        for i in range(1,len(strs)):
            if len(strs[i])<len(min_str):
                min_str=strs[i]
        for i in range(len(min_str)):
            for j in range(1,len(strs)):
                if strs[0][i]!=strs[j][i]:
                    return strs[0][:i]
        return min_str
        