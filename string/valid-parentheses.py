class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={}
        hashmap["{"]="}"
        hashmap["("]=")"
        hashmap["["]="]"
        n=len(s)
        st=[]
        for i in range(n):
            if s[i] in hashmap:
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                ch=hashmap[st.pop()]
                if ch != s[i]:
                    return False
        return len(st)==0



        