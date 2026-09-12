class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices=sorted(prices,reverse=True)
        discounts=sorted(discounts,reverse=True)
        #print(prices)
        #print(discounts)
        p1=0
        p2=0
        n=len(prices)
        m=len(discounts)
        while p1 < n and p2 < m:
            prices[p1]=(prices[p1]*(100-discounts[p2]))/100
            #print(prices[p1])
            p1+=1
            p2+=1
        ans=sum(prices)
        return ans