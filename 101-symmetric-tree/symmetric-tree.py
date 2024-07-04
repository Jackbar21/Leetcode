# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
    
    def isPalindrome(self, arr):
        if len(arr) <= 1:
            return True
        
        l, r = 0, len(arr) - 1

        while l < r:
            if arr[l] != arr[r]:
                return False
            
            l += 1
            r -= 1
        
        return True
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.generateValues(root, 0)
        for arr in self.d.values():
            if not self.isPalindrome(arr):
                return False
        
        return True
    
    def generateValues(self, root, depth):
        if not root:
            if depth not in self.d:
                self.d[depth] = []
            self.d[depth].append(-101)
            return
        
        self.generateValues(root.left, depth + 1)
        if depth not in self.d:
            self.d[depth] = []
        self.d[depth].append(root.val)

        self.generateValues(root.right, depth + 1)