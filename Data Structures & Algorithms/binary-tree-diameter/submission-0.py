# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(curr): # returns height
            if not curr:
                return 0
            
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)

            nonlocal result
            result = max(result, left_height + right_height)
            return 1 + max(left_height, right_height)

        dfs(root)    
        return result


