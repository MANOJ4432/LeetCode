class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        count=[0]*(501)
        def bad(x):
            #case 1:
            for a in range(1,x):
                b=x-a
                if a == b:
                    if count[a]>=2:
                        return True
                else:
                    if count[a] and count[b]:
                        return True
            #case 2:
            for a in range(1,501-x):
                #a,a+x
                if a == x:
                    if count[a] >=2 and count[a+x]:
                        return True
                else:
                    if count[a] and count[a+x]:
                        return True

            return False
        l=0
        best=0
        for r,x in enumerate(nums):
            count[x]+=1
            while bad(x):
                count[nums[l]]-=1
                l+=1
            best=max(best,r-l+1)
        return best

"""
       if you are adding one element to the valid window 
       there are 2 invalid cases
       1.
       a+b=x
       a E window and b E window 
       not valid
       so check for a and x-a in the window
       2.
       a+x=b
       a E window and b E window
       not valid 
       so check for a and a+x in the window
       """
"""
       How we check this the big thing actually
       Take a count array since 1<=nums[i]<=500
       at max we can have a size 501 count arr which is in the constraints limit
       in case 1
       if a == b:
        means a==x-a then count[a] >= 2 (atleat twice ) in the window 
        in case 2
        if a == x then count x >= 2:
            and check for a+x """
