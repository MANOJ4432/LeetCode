class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n=len(nums)
        v=int(1e5+1)
        diff=[0]*v
        nonzero=0
        for x in nums:
            diff[x]+=1
        for x in target:
            diff[x]-=1
        nonzero=sum(1 for x in diff if x!=0)
        sorted_suffix=[True]*n
        for i in range(n-2,-1,-1):
            sorted_suffix[i]=(sorted_suffix[i+1] and target[i] >= target[i+1])
        count=0
        pre_equal=True
        for i in range(n):
            if pre_equal and sorted_suffix[i] and nonzero==0:
                count+=1
            if nums[i]!=target[i]:
                x=nums[i]
                old=diff[x]
                diff[x]-=1
                if old == 1:
                    nonzero-=1
                elif old == 0:
                    nonzero+=1
                x=target[i]
                old=diff[x]
                diff[x]+=1
                if old == -1:
                    nonzero-=1
                elif old == 0:
                    nonzero+=1
            if nums[i]!=target[i]:
                pre_equal=False
        return count