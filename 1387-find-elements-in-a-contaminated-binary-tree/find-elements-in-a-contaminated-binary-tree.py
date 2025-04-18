# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        stack = [(root, 0)]
        while stack:
            treeNode, x = stack.pop()
            self.nums.add(x)
            if (leftNode := treeNode.left):
                stack.append((leftNode, 2 * x + 1))
            if (rightNode := treeNode.right):
                stack.append((rightNode, 2 * x + 2))
        
    def find(self, target: int) -> bool:
        return target in self.nums

            

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)