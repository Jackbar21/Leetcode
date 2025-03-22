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

        # print(f"{preorder=}")
        # content = ",".join(preorder)
        # res = f"[{','.join(preorder)}]"
        # print(f"{res=}")
        while preorder and preorder[-1] == "null":
            preorder.pop()
        res = ",".join(preorder)
        print(f"Serialize: {res=}")
        return res
            


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        des = data.split(",")
        N = len(des)
        
        index_to_node = defaultdict(lambda: None)
        for index, value in enumerate(des):
            # if value == "null":
            #     index_to_node[index] = None
            #     continue
            if value == "null":
                continue
            
            node = TreeNode(int(value))
            index_to_node[index] = node
        
        print(f"{N=}, {len(des)=}, {len(index_to_node)=}")
        print(f"{index_to_node=}")
        queue = collections.deque([index_to_node[0]])
        queue_index = 0
        queue_left = True
        for index in range(1, N):
            node = index_to_node[index]
            queue_node = queue[queue_index]
            if queue_left:
                queue_node.left = node
                queue_left = False
            else:
                queue_node.right = node
                queue_index += 1
                queue_left = True

            if not node:
                continue
            queue.append(node)
        
        return queue[0]

        for index in range(N):
            node = index_to_node[index]
            if not node:
                continue
            left_child = index_to_node[2 * index + 1]
            right_child = index_to_node[2 * index + 2]

            node.left = left_child
            node.right = right_child
        
        # print(f"{index_to_node}")
        res = index_to_node[0]
        print(f"Deserialize: {res}")
        return res
        # [1,2,3,null,null,4,5,6,7]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))