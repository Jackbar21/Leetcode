class Solution:
    def bigger(self, num_a: str, num_b: str):
        # e.g. num_a == 34, num_b == 30000
        # 3430000 > 3000034
        return num_a if (num_a + num_b > num_b + num_a) else num_b
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums =  self.largestNumberHelper(nums)
        # If biggest number is 0, then all numbers are 0, and
        # X number of 0s concatenated together is simply just 0.
        if sorted_nums[0] == "0":
            return "0"
        return ''.join(str(num) for num in sorted_nums)
    def largestNumberHelper(self, nums, depth = 0):
        groups = {digit: [] for digit in "0123456789"}
        for num in nums:
            group = str(num)[0]
            groups[group].append(str(num))

        sorted_nums = []
        for level in "9876543210":
            sorted_level = self.magicSort(groups[level], 0, len(groups[level]) - 1)
            sorted_nums.extend(sorted_level)

        return sorted_nums
          
    def magicSort(self, arr: List[int], i, j) -> List[int]:
        # At this point, arr represents a certain "level". To make explanation easier,
        # suppose this is level "3".
        # Any other level larger than 3, i.e. 4-9, we can assume to have already been "cleared".
        # This is because any number with a leading digit greater than 3, should be in front
        # (to the small) of any number whose leading digit is less than or equal to 3, in order
        # to maximize the final number. Therefore, we can assume at this stage, that any other
        # number with a leading digit greater than three has already been "cleared"/"considered"
        # and can be safely assumed to "not exist".

        # Idea: we will take all length 1 digits as our "pivot" (there can be 0, 1, or more than
        # one such digits). They will be placed in the "middle" of our result array.
        # In the "small" side of our result array, will be number whose second digit
        if i >= j:
            return [arr[i]] if i == j else []

        # mid = len(arr)//2
        mid = (i + j + 1) // 2
        # left, right = arr[:mid], arr[mid:]
        # left = self.magicSort(left)
        # right = self.magicSort(right)
        # print(i, j, mid)
        left = self.magicSort(arr, i, mid - 1)
        right = self.magicSort(arr, mid, j)
        print(left, right)

        # Idea: we now have "sorted" versions of left and right. We want to essentially
        # always pick the "better" element from either the beginning of left or right,
        # better meaning that it will yield an overall larger number, therefore the 
        # best we can do for our current level in regards to having highest significant
        # digit values. We do this via our 'better' function, which concatenates two
        # numbers together, to check which ordering of concatenation yields the overall
        # larger number.
        res = []
        l, r = 0, 0
        while l < len(left) and r < len(right):
            # print(r, j, right)
            bigger = self.bigger(left[l], right[r])
            if bigger == left[l]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        
        # assert not ((l < len(left)) and (r < len(right)))
        if l < len(left):
            res.extend(left[l:])
        elif r < len(right):
            res.extend(right[r:])
        
        print(res)
        return res
