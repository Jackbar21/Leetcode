class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pre, eq, post = [], [], []
        for num in nums:
            (
                pre if num < pivot else
                eq if num == pivot else
                post
            ).append(num)
        return pre + eq + post