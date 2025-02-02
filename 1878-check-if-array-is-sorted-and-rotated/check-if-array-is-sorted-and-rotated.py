class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        nextIndex = lambda index: (index + 1) % N

        # smallest_num = float("inf")
        # smallest_index = None
        # for i, num in enumerate(nums):
        #     if num <= smallest_num:
        #         smallest_num = num
        #         smallest_index = i

        for index in range(N):
            prev_num = nums[index]
            res = True
            for _ in range(N):
                num = nums[index]
                print(f"{prev_num=}, {num=}, {index=}")
                if prev_num > num:
                    res = False
                    break

                # Loop Invariant
                prev_num = num
                # index = nextIndex(index)
                index += 1
                index %= N
            
            if res:
                return True
        
        return False