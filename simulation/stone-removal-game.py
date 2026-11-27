AliceWins=[False]*51
counter=10
i=10
while i > 2:
    if i & 1:
        print(i)
        j=0
        while j < i and counter <= 50:
            print(counter)
            AliceWins[counter]=True
            counter+=1
            j+=1
        counter=counter+i-1
    i-=1

class Solution:
    def canAliceWin(self, n: int) -> bool:
        return AliceWins[n]

            
