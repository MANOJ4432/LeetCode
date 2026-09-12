import heapq
def prims(graph,n):
    vis=[False]*(n)
    pq=[]
    cost=0
    heapq.heappush(pq,(0,-1,0))
    while len(pq)!=0:
        data=heapq.heappop(pq)
        node=data[2]
        if vis[node] == True:
            continue
        vis[node]=True
        cost+=data[0]
        for neigh in graph[node]:
            if vis[neigh[0]] == False:
                heapq.heappush(pq,(neigh[1],node,neigh[0]))
    return cost

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
            n=len(points)
            graph=[]
            for _ in range(n):
                graph.append([])
            for i in range(n-1):
                for j in range(i+1,n):
                    dis=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    graph[i].append((j,dis))
                    graph[j].append((i,dis))
            return prims(graph,n)