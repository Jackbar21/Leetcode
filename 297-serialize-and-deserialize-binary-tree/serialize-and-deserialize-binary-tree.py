# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        queue = collections.deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            if not node:
                preorder.append("null")
                continue
            preorder.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        while preorder and preorder[-1] == "null":
            preorder.pop()
        res = ",".join(preorder)
        return res
            


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        des = data.split(",")
        
        nodes = []
        for index, value in enumerate(des):
            if value == "null":
                nodes.append(None)
                continue

            node = TreeNode(int(value))
            nodes.append(node)
        
        queue = collections.deque([nodes[0]])
        queue_left = True
        for index in range(1, len(nodes)):
            node = nodes[index]
            queue_node = queue[0]
            if queue_left:
                queue_node.left = node
                queue_left = False
            else:
                queue_node.right = node
                queue.popleft()
                queue_left = True

            if node is not None:
                queue.append(node)
        
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
