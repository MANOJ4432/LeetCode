class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        nums.sort()
        mod=int(1e9+7)
        new_k=k
        cost=0
        for i in range(len(nums)):
            if new_k < nums[i]:
                print(new_k,i)
                x=(nums[i]-new_k)//k
                if (nums[i]-new_k)%k == 0:
                    cost=cost+x
                    new_k=0
                else:
                    cost=cost+x+1
                    new_k=new_k+(x+1)*k-nums[i]
            else:
                new_k-=nums[i]
        return (cost*(cost+1)//2)%int(1e9+7)
        