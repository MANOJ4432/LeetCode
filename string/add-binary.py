class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int(a,2)
        b=int(b,2)
        c=a+b
        c=bin(c)
        return c[2:]