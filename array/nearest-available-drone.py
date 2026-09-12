class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        arr=[]
        n=len(drones)
        mini=-1
        min_dis=float("inf")
        for i in range(n):
            x=abs(drones[i][0]-target[0])+abs(drones[i][1]-target[1])
            if x <= drones[i][2] and x < min_dis:
                min_dis=x
                mini=i
        return mini
            