class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            new_res = []
            for lst in res:
                new_lst = lst.copy()
                new_lst.append(num)
                new_res.append(new_lst)
            res.extend(new_res)
        
        return res