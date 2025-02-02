class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)

        smallest_num = float("inf")
        smallest_indices = []
        for i, num in enumerate(nums):
            if num < smallest_num:
                smallest_num = num
                smallest_indices = [i]
            elif num == smallest_num:
                smallest_indices.append(i)

        for smallest_index in smallest_indices:
            index = smallest_index
            prev_num = nums[index]
            is_sorted = True
            for _ in range(N):
                num = nums[index]
                if prev_num > num:
                    is_sorted = False
                    break

                # Loop Invariant
                prev_num = num
                index = (index + 1) % N
            
            if is_sorted:
                return True
        
        return False