class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)

        if k==n:
            return max(nums)
        if k==1:
            #without duplicates
            hm={}
            for i in range(n):
                if nums[i] in hm:
                    hm[nums[i]]+=1
                else:
                    hm[nums[i]]=1
            maxi=-1
            for key,count in hm.items():
                if count == 1:
                    maxi=max(maxi,key)
            return maxi  
        c1=0
        c2=0
        val1=nums[0]
        val2=nums[n-1]
        for i in range(n):
            if nums[i] == val1:
                c1+=1
            if nums[i]==val2:
                c2+=1
        if c1==1 and c2==1:
            return max(val1,val2)
        if c1 > 1 and c2==1:
            return val2
        if c2 > 1 and c1==1:
            return val1
        return -1


            