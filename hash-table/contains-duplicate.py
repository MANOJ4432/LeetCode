class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pure=set(nums)
        if len(nums)==len(pure):
            return False
        return True
        """for x in nums:
            if x in pure:
                return True
            pure.add(x)
        return False"""

