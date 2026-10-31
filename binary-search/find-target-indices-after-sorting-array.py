class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        targetList=[]
        #insertion sort
        n=len(nums)
        equalelements=0
        greaterelements=0
        for i in range(n):
            if nums[i] > target:
                greaterelements+=1
            elif nums[i] == target:
                equalelements+=1
        if equalelements == 0:
            return []
        i=n-(equalelements+greaterelements)
        while equalelements !=0 :
            targetList.append(i)
            equalelements-=1
            i+=1
        return targetList


                
