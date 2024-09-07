# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if (head, root) in self.memo:
            return self.memo[(head, root)]

        if not head:
            return True
        
        if not root:
            return False
        
        if head.val == root.val:
            if (self.isDirectSubPath(head.next, root.left) or 
                self.isDirectSubPath(head.next, root.right)
            ):
                self.memo[(head, root)] = True
                return True
        
        self.memo[(head, root)] = (
            self.isSubPath(head, root.left) or 
            self.isSubPath(head, root.right)
        )
        return self.memo[(head, root)]
    
    def isDirectSubPath(self, head, root):
        if not head:
            return True
        
        if not root:
            return False
        
        if head.val != root.val:
            return False
        
        return (self.isDirectSubPath(head.next, root.left) or 
                self.isDirectSubPath(head.next, root.right))