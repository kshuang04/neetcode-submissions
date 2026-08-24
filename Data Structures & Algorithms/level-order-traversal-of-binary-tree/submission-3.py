# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        result = []

        while q:
            level_length = len(q)
            curr_level = []
            for i in range(level_length):
                node = q.popleft()
                if node:
                    curr_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curr_level:
                result.append(curr_level)
        
        return result