def digitsum(integer):
    digi_sum=0
    while integer!=0:
        digi_sum+=integer%10
        integer//=10
    return digi_sum
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        end=10**n
        ans=-1
        for i in range(end):
            #print(i)
            x=digitsum(i)
            #print(i," ",x)
            if x==s:
                ans=max(ans,i)
        return ans
        