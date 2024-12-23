# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)

        queue = collections.deque([(root, 1)]) # (node, level)
        while len(queue) > 0:
            node, level = queue.popleft()
            d[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return sum(self.getNumSwapsNeededToMakeSorted(values) for values in d.values())
    
    def getNumSwapsNeededToMakeSorted(self, nums):
        num_to_index, index_to_num = {}, {}
        for i, num in enumerate(nums):
            num_to_index[num] = i
            index_to_num[i] = num

        num_swaps = 0
        for correct_index, num in enumerate(sorted(nums)):
            num_index = num_to_index[num]
            if num_index == correct_index:
                continue

            # Otherwise, num's index should be made to correct index, which
            # obviously requires a swap with the number that's ACTUALLY at correct index!
            num_at_correct_index = index_to_num[correct_index]

            # Make a swap!
            idx1, num1 = num_index, num
            idx2, num2 = correct_index, num_at_correct_index

            # assert index_to_num[idx1] == num1
            # assert index_to_num[idx2] == num2
            # assert num_to_index[num1] == idx1
            # assert num_to_index[num2] == idx2
            index_to_num[idx1] = num2
            index_to_num[idx2] = num1
            num_to_index[num1] = idx2
            num_to_index[num2] = idx1
            num_swaps += 1

        return num_swaps
