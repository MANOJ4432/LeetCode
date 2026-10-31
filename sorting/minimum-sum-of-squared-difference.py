import heapq
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        d = sorted((abs(a - b) for a, b in zip(nums1, nums2)), reverse=True)
        k=k1+k2
        if sum(d) <= k:
            return 0

        n=len(d)
        d.append(0)
        for i in range(n):
            cnt=i+1
            cost=(d[i]-d[i+1])*cnt
            if k >= cost:
                k-=cost
                continue
            q=k//cnt
            r=k%cnt
            level=d[i]-q
            ans=r*(level-1)*(level-1)+(cnt-r)*level*level
            ans+=sum(x*x for x in d[i+1:n])
            return ans