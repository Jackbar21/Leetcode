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
        
        res = False
        if head.val == root.val:
            if self.isDirectSubPath(head.next, root.left) or self.isDirectSubPath(head.next, root.right):
                print("TRUTH1")
                res = True
        
        res = res or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        if res:
            print("TRUTH2")
        self.memo[(head, root)] = res
        return res
    
    def isDirectSubPath(self, head, root):
        if not head:
            return True
        
        if not root:
            return False
        
        if head.val != root.val:
            return False
        
        if self.isDirectSubPath(head.next, root.left):
            return True
        
        if self.isDirectSubPath(head.next, root.right):
            return True
        
        return False
