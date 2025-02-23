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
            # Already seen node, so keep deleting nodes in stack
            # until we reach this seen node, delete it, and continue
            # adding nodes from top of the stack THEN.
            if (val := postorder[post_index]) in visited:
                while stack.pop().val != val:
                    pass
                post_index += 1
                continue

            target_val = postorder[post_index]
            while (val := preorder[pre_index]) != target_val:
                node = TreeNode(val)
                # assert val not in visited
                visited.add(val)
                prev_node = stack[-1]
                if not prev_node.left:
                    prev_node.left = node
                else:
                    #assert not prev_node.right
                    prev_node.right = node

                stack.append(node)
                pre_index += 1
                val = preorder[pre_index]

            # One more time
            node = TreeNode(val)
            # assert val not in visited
            visited.add(val)
            prev_node = stack[-1]
            if not prev_node.left:
                prev_node.left = node
            else:
                #assert not prev_node.right
                prev_node.right = node

            stack.append(node)
            pre_index += 1

            # Finally visited target val, so continue from here
            post_index += 1
            stack.pop()
        
        return root
