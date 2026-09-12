class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)
        nums=[0]*(n+m)
        idx=0
        p1,p2=0,0
        while(p1<n and p2<m):
            if nums1[p1] < nums2[p2]:
                nums[idx]=nums1[p1]
                idx+=1
                p1+=1
            else:
                nums[idx]=nums2[p2]
                idx+=1
                p2+=1
        while(p1<n):
                nums[idx]=nums1[p1]
                idx+=1
                p1+=1
        while(p2<m):
                nums[idx]=nums2[p2]
                idx+=1
                p2+=1
        
        x=(n+m)//2
        if (n+m)%2!=0:
            return nums[x]
        else:
            
            return (nums[x]+nums[x-1])/2

