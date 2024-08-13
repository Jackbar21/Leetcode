

# [], target = 5

# [], target = 5
# [2], target = 3

# [], target = 5
# [5], target = 0 ding ding ding
# [2], target = 3
# [2,5], target = -2
class Solution:
    def __init__(self):
        self.memo = {} # cache (i, target), i represents candidates[:i]
        self.candidates = None
        self.target = -1
        self.solutions = {} # contains arrays mapping to sums
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # self.candidates, self.target = candidates, target
        # return self.combinationSumHelper(len(candidates), target)
        candidates.sort()
        solutions = set()
        i = 0
        current_solution = []
        ban_list = defaultdict(int)
        def backtrackHelper(i, current_sum):
            if current_sum == target:
                solutions.add(tuple(current_solution))
            if i >= len(candidates) or current_sum > target:
                return

            # print(current_solution)

            current_solution.append(candidates[i])
            if current_sum + candidates[i] <= target and ban_list.get(candidates[i], 0) <= 0:
                backtrackHelper(i + 1, current_sum + candidates[i])
            current_solution.pop()
            ban_list[candidates[i]] += 1
            backtrackHelper(i + 1, current_sum)
            ban_list[(candidates[i])] -= 1
            return

        backtrackHelper(0, 0)
        return solutions



    

    # def combinationSumHelper(self, i, target):
    #     if target < 0:
    #         return []
        
    #     if target == 0:

        
    #     if (i, target) in self.memo:
    #         return self.memo[(i, target)]

    #     # Case 1: Include the i'th element
    #     #candidates[:i] which we've solved
    #     target - candidates[i]
    #     self.combinationSumHelper(i - 1)



    #     # Case 2: Don't include the i'th element
        

    #     #candidates[:-1], target
    #     #candidates[:-1], target - candidates[0]

    #     return self.memo[(i, target)]