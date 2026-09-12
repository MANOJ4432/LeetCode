class Node:
    def __init__(self,data):
        self.data=data
        self.child=[]
def constructTree(root,parents):
    hm={}
    root=Node(0)
    hm[0]=root
    for i in range(1,len(parents)):
        if parents[i] in hm:
            if i not  in hm:
                newnode=Node(i)
                hm[i]=newnode
        else:
            newnode=Node(parents[i])
            hm[parents[i]]=newnode
            if i not in hm:
                newnod=Node(i)
                hm[i]=newnod
        hm[parents[i]].child.append(hm[i])
    return root
def height(root,th,h):
    if len(root.child)==0:
        h[0]=max(h[0],th)
        return 
    size=len(root.child)
    for i in range(size):
        height(root.child[i],th+1,h)
def weight(root,d,ans,nums,h):
    w=nums[root.data]*(h[0]-d+1)
    ans[0]+=w
    if len(root.child)==0:
        return 
    size=len(root.child)
    for i in range(size):
        weight(root.child[i],d+1,ans,nums,h)
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        root=None
        root=constructTree(root,parent)
        h=[0]
        height(root,1,h)
        ans=[0]
        weight(root,1,ans,nums,h)
        return ans[0]
        
        