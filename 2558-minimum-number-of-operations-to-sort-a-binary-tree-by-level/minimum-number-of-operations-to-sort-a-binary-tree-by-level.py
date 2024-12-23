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
        # For every index i in nums, want to find index j such that nums[j] == min(nums[i+1:])
        # Note that all values in the tree are unique, so don't need to do things based off
        # indices :)
        # sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])
        sorted_nums = sorted(nums)
        # print(f"{sorted_nums=}")
        # print(f"{nums=}")

        num_to_index = {num: i for i, num in enumerate(nums)}
        index_to_num = {i: num for i, num in enumerate(nums)}

        num_swaps = 0
        for correct_index, num in enumerate(sorted_nums):
            num_index = num_to_index[num]
            if num_index == correct_index:
                continue

            # Otherwise, num's index should be made to correct index, which
            # obviously requires a swap with the number that's ACTUALLY at correct index!
            num_at_correct_index = index_to_num[correct_index]

            # Make a swap!
            idx1, num1 = num_index, num
            idx2, num2 = correct_index, num_at_correct_index

            assert index_to_num[idx1] == num1
            assert index_to_num[idx2] == num2
            assert num_to_index[num1] == idx1
            assert num_to_index[num2] == idx2
            index_to_num[idx1] = num2
            index_to_num[idx2] = num1
            num_to_index[num1] = idx2
            num_to_index[num2] = idx1
            num_swaps += 1

        return num_swaps

        for i, num in enumerate(nums):
            sorted_num = sorted_nums[i]
            if num == sorted_num:
                continue
            
            # nums[i] != sorted_nums[i]. 
            # assert i < 

        num_to_index = {
            num: i for i, num in enumerate(nums)
        }
        res = 0
        # print(f"{num_to_index=}")
        made_good = set()
        for i, num in enumerate(nums):
            sorted_num = sorted_nums[i]
            if num_to_index[num] == num_to_index[sorted_num]:
                continue
            
            if sorted_num in made_good:
                continue
            
            num_idx, sorted_idx = num_to_index[num], num_to_index[sorted_nums[i]]
            # print(f"{num=}, {sorted_nums[i]=}, {num_idx=}, {sorted_idx=}")
            res += 1
            num_to_index[num] = sorted_idx
            num_to_index[sorted_num] = num_idx
            made_good.add(num)
            made_good.add(sorted_num)
        
        # print(f"{num_to_index=}")


        # return math.ceil(sum(nums[i] != sorted_nums[i] for i in range(len(nums))) / 2)
        return res

        made_good = set()
        num_swaps = 0
        for i in range(len(nums)):
            index = i
            num = nums[i]
            # if num in made_good:
            #     continue

            sorted_num, sorted_index = sorted_nums[i]
            if num != sorted_num:
                nums[index], nums[sorted_index] = nums[sorted_index], nums[index]
                # nums = [5,6,8,7]
                
    
            sorted_num = sorted_nums[i]
            if num != sorted_num:
                res += 1

            # if index != sorted_index:
            #     nums[index], nums[sorted_index] = nums[sorted_index], nums[index]

        return num_swaps