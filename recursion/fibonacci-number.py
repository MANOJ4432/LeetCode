n=31
fibo=[0]*n
fibo[0],fibo[1]=0,1
for i in range(2,n):
    fibo[i]=fibo[i-1]+fibo[i-2]
class Solution:
    def fib(self, n: int) -> int:
        return fibo[n]