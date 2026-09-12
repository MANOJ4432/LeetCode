class Solution:

  def divide(self, dividend: int, divisor: int) -> int:
    self.dividend=dividend
    self.divisor=divisor
    if(self.dividend== self.divisor):
        return 1
    sign=True
    if( self.dividend>=0 and  self.divisor<0):
        sign=False
    elif( self.dividend<=0 and  self.divisor>0):
        sign=False
    self.dividend=abs( self.dividend)
   
    self.divisor=abs( self.divisor)
   
    ans=0
    while( self.dividend>= self.divisor):
        c=0
        while( self.dividend>= self.divisor<<c):
            c+=1
        c-=1
        ans+=1<<c
       
        self.dividend-= self.divisor<<c
    if(sign and ans>=pow(2,31)):
        return pow(2,31)-1
    elif(not sign and ans>pow(2,31)):
        return pow(-2,31)
    elif(sign):
        return ans
    else:
        return -1*ans