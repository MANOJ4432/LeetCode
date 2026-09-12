# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxpathSum(root,ans):
    if root is None:
        return 0
    x=maxpathSum(root.left,ans)
    y=maxpathSum(root.right,ans)
    curr=x+y+root.val
    #print(curr,end=" ")
    ans[0]=max(ans[0],curr)
    return max(0,max(x,y)+root.val)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[float("-inf")]
        maxpathSum(root,ans)
        return ans[0]

        