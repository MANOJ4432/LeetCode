# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def pushLeft(st,root):
            while root:
                st.append(root)
                root=root.left
        def pushRight(st,root):
            while root:
                st.append(root)
                root=root.right
        def nextLeft(st):
            node=st.pop()
            pushLeft(st,node.right)
            return node.val
        def nextRight(st):
            node=st.pop()
            pushRight(st,node.left)
            return node.val
        stLeft,stRight=[],[]
        pushLeft(stLeft,root)
        pushRight(stRight,root)
        l=nextLeft(stLeft)
        h=nextRight(stRight)
        while l < h:
            if (l+h) == k:
                return True
            elif l + h < k:
                l=nextLeft(stLeft)
            else:
                h=nextRight(stRight)
        return False
