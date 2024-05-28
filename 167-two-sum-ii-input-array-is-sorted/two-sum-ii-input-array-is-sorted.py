class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        # while numbers[right] > target:
        #     right -= 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                # need to make sum smaller, so 
                # decrement right pointer by 1
                right -= 1
            else:
                # need to make sum larger, so
                # increment left pointer by 1
                left += 1
        
        return sorted([left + 1, right + 1])