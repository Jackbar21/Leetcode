# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return (self.isValidBSTHelper(root.left, root.val, root.val) 
        # and self.isValidBSTHelper(root.right, root.val, root.val))
        return self.isValidHelper(root, float("-inf"), float("inf"))
    
    def isValidHelper(self, root, lower_bound, upper_bound):
        if not root:
            return True
        
        if not (lower_bound <= root.val <= upper_bound):
            return False
        
        return (
            self.isValidHelper(root.left, lower_bound, min(upper_bound, root.val - 1))
            and self.isValidHelper(root.right, max(lower_bound, root.val + 1), upper_bound)
        )
        
    
    def isValidBSTHelper(self, root, smallest, largest):
        if not root:
            return True
        

        
        smallest = min(smallest, root.val)
        largest = max(smallest, root.val)


        
        # if not root.left and not root.right:
        #     return True
        
        if root.left:
            if not (root.left.val < root.val):
                return False
            if root.left.val <= largest:
                return False
        
        if root.right:
            if not (root.right.val > root.val):
                return False
            if root.right.val >= smallest:
                return False
        
        # Update smallest & largest
        smallest = min(smallest, root.val)
        largest = max(largest, root.val)
        return (self.isValidBSTHelper(root.left, smallest, largest) 
        and self.isValidBSTHelper(root.right, smallest, largest))