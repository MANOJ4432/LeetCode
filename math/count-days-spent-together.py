class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        noofdays=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        psum=[0]*12
        for i in range(1,12):
            psum[i]=psum[i-1]+noofdays[i-1]
        #decoding dates
        days=[]
        days.append(generateToken(arriveAlice,psum))
        days.append(generateToken(leaveAlice,psum))
        days.append(generateToken(arriveBob,psum))
        days.append(generateToken(leaveBob,psum))
        if days[1] < days[2] or days[3] < days[0]:
            return 0
        days.sort()
        return days[2]-days[1]+1
def generateToken(x,psum):
    x=list(map(int,x.split("-")))
    return psum[x[0]-1]+x[1]

        