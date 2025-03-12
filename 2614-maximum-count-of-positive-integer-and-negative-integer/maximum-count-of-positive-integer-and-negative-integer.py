class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # return max(sum(num > 0 for num in nums), sum(num < 0 for num in nums))
        # pos, neg = 0, 0
        # for num in nums:
        #     if num > 0:
        #         pos += 1
        #     elif num < 0:
        #         neg += 1
        # return max(pos, neg)

        # I COMPLETELY didn't realize this array was sorted... 
        N = len(nums)
        # Step 1: Find rightmost index of negative integer (if any exist)
        neg = 0
        if nums[0] < 0: # Check there's at least one negative integer
            rightmost_index = 0
            l, r = 0, N - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < 0:
                    # Valid solution, search for even larger indices (if any)!
                    rightmost_index = max(rightmost_index, mid)
                    l = mid + 1
                else:
                    # Invalid solution, search left for any existing solutions.
                    r = mid - 1

            # Last negative number is at index 'rightmost_index', and first at index 0.
            # Hence there are: (rightmost_index) - (0) + 1 == rightmost_index + 1 negative numbers.
            neg = rightmost_index + 1
        
        # Step 2: Find leftmost index of positive integer (if any exist)
        pos = 0
        if nums[N - 1] > 0: # Check there's at least one positive integer
            leftmost_index = N - 1
            l, r = 0, N - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > 0:
                    # Valid solution, search for even smaller indices (if any)!
                    leftmost_index = min(leftmost_index, mid)
                    r = mid - 1
                else:
                    # Invalid solution, search right for any existing solutions.
                    l = mid + 1

            # Last positive number is at index N - 1, and first at index 'leftmost_index'.
            # Hence there are: (N - 1) - (leftmost_index) + 1 == N - leftmost_index positive numbers.
            pos = N - leftmost_index
        
        return max(pos, neg)