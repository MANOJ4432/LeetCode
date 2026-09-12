class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>=0:
            if n==0:
                return 1
            val=self.myPow(x,n//2)
            if n%2==0:

                return val*val
            else:
                return val*val*x
        else:
            if n==0:
                return 1/x
            val=self.myPow(x,(n+1)//2)
            if n%2==0:
                return val*val
            else:
                return val*val*(1/x)
