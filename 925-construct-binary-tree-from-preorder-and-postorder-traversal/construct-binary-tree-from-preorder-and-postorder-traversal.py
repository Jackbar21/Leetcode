# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Setup Work
        pre_index, post_index = 0, 0
        root = TreeNode(preorder[pre_index])
        pre_index += 1
        stack = [root]
        visited = set() # values, not nodes!
        visited.add(root.val)

        while post_index < len(postorder):
            if (val := postorder[post_index]) in visited:
                post_index += 1
                while stack.pop().val != val:
                    pass
                continue
        # for i in range(1):
            #print(f"{pre_index=}, {post_index=}")
            while (val := preorder[pre_index]) != postorder[post_index]:
                node = TreeNode(val)
                #assert val not in visited
                visited.add(val)
                prev_node = stack[-1]
                # #assert not prev_node.left
                if not prev_node.left:
                    prev_node.left = node
                else:
                    #assert not prev_node.right
                    prev_node.right = node
                # stack[-1].left = node
                stack.append(node)
                
                pre_index += 1
            # One more time
            node = TreeNode(val)
            #assert val not in visited
            visited.add(val)
            # stack[-1].left = node
            prev_node = stack[-1]
            if not prev_node.left:
                prev_node.left = node
            else:
                #assert not prev_node.right
                prev_node.right = node
            stack.append(node)
            pre_index += 1
            post_index += 1
            
            # stack.append(preorder[pre_index])
            # pre_index += 1
            # post_index += 1

            # #print(f"{val_to_node=}")
            # #print(f"{stack=}")
            #print("STACK START")
            # for line in stack:
                #print(f"node={line}")
            #print("STACK END")
            #print(f"{preorder[pre_index:]=}")
            #print(f"{postorder[post_index:]=}")

            stack.pop()
        
        return root
