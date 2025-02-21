# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        # self.nums = set()
        # def inorder(treeNode, x):
        #     if treeNode is None:
        #         return
            
        #     inorder(treeNode.left, 2 * x + 1)
        #     self.nums.add(x)
        #     inorder(treeNode.right, 2 * x + 2)
        # inorder(root, 0)
        nums = set()
        stack = [(root, 0)]
        while stack:
            treeNode, x = stack.pop()
            nums.add(x)
            if treeNode.left:
                stack.append((treeNode.left, 2 * x + 1))
            if treeNode.right:
                stack.append((treeNode.right, 2 * x + 2))
        self.nums = nums
        
    def find(self, target: int) -> bool:
        return target in self.nums    

            

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)