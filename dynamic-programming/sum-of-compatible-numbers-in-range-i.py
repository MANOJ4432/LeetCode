class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum=0
        for x in range(n-k,n+k+1):
            if x>0 and abs(n-x)<=k and n&x==0:
                sum+=x
        return sum
                