# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        self.max_num = 0
        def inorder(treeNode, x):
            if treeNode is None:
                return
            
            inorder(treeNode.left, 2 * x + 1)
            self.nums.add(x)
            self.max_num = max(self.max_num, x)
            inorder(treeNode.right, 2 * x + 2)
        inorder(root, 0)
        # print(f"{sorted(self.nums)=}, {self.max_num=}")
        # self.root = root
        
    def find(self, target: int) -> bool:
        if target > self.max_num:
            return False
        return target in self.nums
        val = 0
        node = self.root
        while node:
            if node.val == -1:
                node.val = val
            assert node.val == val
            if val == target:
                return True
            

            

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)