# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # First idea: just get all the elements, heapify array, and pop k times
        # for total complexity of O(n + klogn)
        self.populateArr(root)

        # Nevermind, as I got here I realized I can just add elements inorder,
        # and return self.arr[k]
        return self.arr[k-1]
    
    def populateArr(self, root):
        if not root:
            return
        
        self.populateArr(root.left)
        self.arr.append(root.val)
        self.populateArr(root.right)