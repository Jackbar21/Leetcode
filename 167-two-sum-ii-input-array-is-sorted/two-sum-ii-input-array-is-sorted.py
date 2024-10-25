class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            num1, num2 = numbers[l], numbers[r]

            if num1 + num2 < target:
                l += 1
            elif num1 + num2 > target:
                r -= 1
            else:
                # assert num1 + num2 == target
                return [l + 1, r + 1]
        
        raise Exception("Unreachable Code")