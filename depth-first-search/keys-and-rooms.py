from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        noofuvr=n
        vis=[False]*n
        q=deque()
        q.append(0)
        noofuvr-=1
        vis[0]=True
        while len(q)!=0:
            x=q.popleft()
            for node in rooms[x]:
                if vis[node]==False:
                    noofuvr-=1
                    vis[node]=True
                    q.append(node)
        return noofuvr == 0
        

