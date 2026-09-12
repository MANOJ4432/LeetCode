def solve(s,n,k,idx,cost,arr):
    if idx==n:
        if valid(s,n) and cost<=k:
            arr.append(s)
        return
    solve(s+"1",n,k,idx+1,cost+idx,arr)
    solve(s+"0",n,k,idx+1,cost,arr)
def valid(s,n):
    for i in range(1,n):
        if s[i]=="1" and s[i-1]=="1":
            return False
    return True
class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        arr=[]
        solve("",n,k,0,0,arr)
        return arr
        


            
            
            
        
        