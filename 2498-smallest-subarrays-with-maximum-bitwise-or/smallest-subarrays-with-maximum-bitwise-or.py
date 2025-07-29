class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        max_or = functools.reduce(lambda x, y: x | y, nums)
        if max_or == 0:
            return [1] * len(nums)

        binary = bin(max_or)[2:]
        # Least significant to most significant digit ordering
        needed = []
        for i, digit in enumerate(binary[::-1]):
            if digit == "1":
                needed.append(i)
        # print(f"{needed=}")
        
        # For each binary digit, track indices of numbers in nums that contain that digit
        d = {digit: [] for digit in range(len(binary))}
        for num_index, num in enumerate(nums):
            binary = bin(num)[2:]
            for binary_index, digit in enumerate(binary[::-1]):
                if digit == "1":
                    d[binary_index].append(num_index)

        answer = []
        for i, num in enumerate(nums):
            # We need all the digits from 'needed'. For each, compute 
            # minimum index j such that j >= i and nums[j] contains that digit
            # in its binary representation. Then we take the maximum of these such
            # index 'j's for each digit, meaning shortest subarray for index i
            # is nums[i..j], of length j - i + 1.
            min_index = float("-inf")
            for digit in needed:
                # For each digit 'digit', we have d[digit] giving us a list of indices of
                # all numbers in nums that include that digit in its binary representation.
                # Apply leftmost binary search to find leftmost (smallest) index whose value
                # is >= i.
                indices = d[digit]
                # print(f"{i=}, {digit=}, {indices=}")
                l, r = 0, len(indices) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if indices[mid] >= i:
                        # Valid index, look for potentially smaller but also valid ones
                        r = mid - 1
                    else:
                        # Invalid index, look for larger but potentially valid ones
                        l = mid + 1
                
                # assert l < len(indices) # Found a valid solution
                min_index = max(min_index, indices[l] if l < len(indices) else indices[-1])
                # if min_index < l:
                #     min_index = l
                # print(f"{l=}, {indices[l] if l < len(indices) else -1} {min_index=}\n")
            
            answer.append(max(1, min_index - i + 1))

        return answer
