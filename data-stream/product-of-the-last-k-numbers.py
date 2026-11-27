class ProductOfNumbers:

    def __init__(self):
        self.stream=[]
        self.pro=[1]
        self.ans=1
        self.zero=-1
    def add(self, num: int) -> None:
        self.stream.append(num)
        if num !=0:
            self.ans*=num
            self.pro.append(self.pro[-1]*num)
        else:
            self.zero=len(self.stream)
            self.ans=1
            self.pro.append(1)
    def getProduct(self, k: int) -> int:
        n=len(self.stream)
        if self.zero!=-1 and self.zero >= n-k+1:
            return 0
        return self.ans//self.pro[n-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)