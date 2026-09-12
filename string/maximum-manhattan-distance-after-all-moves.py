class Solution:
    def maxDistance(self, moves: str) -> int:
        x,y,extra=0,0,0
        for i in range(len(moves)):
            if moves[i]=="U":
                y+=1
            elif moves[i]=="L":
                x-=1
            elif moves[i]=="R":
                x+=1
            elif moves[i]=="D":
                y-=1
            else:
                extra+=1
        return abs(x)+abs(y)+extra
    """when one of the point is origin
    distance=abs(x2)+abs(y2)
    abs(2)=abs(1+(-1)+1+(-1)+1+1)
    so the final answer is abs(x)+abs(y)+extra"""
            