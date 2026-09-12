class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        m=1
        n=len(digits)
        i=1
        while(i<n):
            m*=10
            i+=1
        num=0
        i=0
        while(m>0 and i<n):
            num+=digits[i]*m
            m//=10
            i+=1
        num+=1
        newlist=[]
        while(num>0):
            newlist.append(num%10)
            num//=10
        newlist.reverse()
        return newlist