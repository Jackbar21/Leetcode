class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            small_num, big_num = numbers[l], numbers[r]

            if small_num + big_num < target:
                l += 1
            elif small_num + big_num > target:
                r -= 1
            else:
                # assert small_num + big_num == target
                return [l + 1, r + 1]
        
        raise Exception("Unreachable Code")
