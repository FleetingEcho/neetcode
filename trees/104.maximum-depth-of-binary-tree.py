from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root,0)

    def traverse(self,root,depth):
        if root==None:
            return depth
        depth+=1
        _l=self.traverse(root.left,depth)
        _r=self.traverse(root.right,depth)
        return max(_l,_r)
