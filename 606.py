# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root:
                return None
            answer = str(root.val)
            
            temp = preorder(root.left)
            if temp or root.right:
                answer += "("+(temp if temp!=None else "")+")"
            temp = preorder(root.right)
            if temp:
                answer += "("+temp+")"
            return answer
        answer = preorder(root)
        return answer

        
