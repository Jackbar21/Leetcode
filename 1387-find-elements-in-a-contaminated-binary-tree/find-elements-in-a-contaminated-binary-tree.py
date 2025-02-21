# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        def inorder(treeNode, x):
            if treeNode is None:
                return
            
            self.nums.add(x)
            inorder(treeNode.left, 2 * x + 1)
            inorder(treeNode.right, 2 * x + 2)
            

        inorder(root, 0)
        

    def find(self, target: int) -> bool:
        return target in self.nums
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)