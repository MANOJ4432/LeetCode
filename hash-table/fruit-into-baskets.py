class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n=len(fruits)
        hm={}
        i,j=0,0
        ans=0
        while j < n:
            if fruits[j] not in hm:
                hm[fruits[j]]=0
            hm[fruits[j]]+=1
            if len(hm) > 2:
                hm[fruits[i]]-=1
                if hm[fruits[i]] == 0:
                    del hm[fruits[i]]
                i+=1   
            if len(hm)<=2:
                ans=max(ans,j-i+1)             
            j+=1
        return ans