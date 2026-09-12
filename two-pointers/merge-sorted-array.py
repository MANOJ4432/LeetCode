class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l=nums1[:m]
        k,i,j=0,0,0
        while(i<m and j<n):
            if(l[i]<nums2[j]):
                nums1[k]=l[i]
                k+=1
                i+=1
            elif l[i]>nums2[j]:
                nums1[k]=nums2[j]
                k+=1
                j+=1
            else:
                nums1[k],nums1[k+1]=l[i],nums2[j]
                i+=1
                j+=1
                k+=2
        while(i<m):
            nums1[k]=l[i]
            k+=1
            i+=1
        while(j<n):
            nums1[k]=nums2[j]
            k+=1
            j+=1
        
                
            
        