class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        N = len(nums)
        prefix_sums = []
        cur_sum = 0
        for num in nums:
            cur_sum += num % modulo == k
            prefix_sums.append(cur_sum)
        # is_interesting = lambda i, j: (prefix_sums[j] - (prefix_sums[i - 1] if i - 1 >= 0 else 0)) % modulo == k
        # return sum(is_interesting(i, j) for i in range(N) for j in range(i, N))

        # Okay at this point -- I got stuck, and chose to look at the hints. Hints 1-4 are useless
        # for me, but Hint #5 denotes something interesting:
        #     prefix_sums[j] - prefix_sums[i - 1] % modulo == k
        # <-> prefix_sums[i - 1] = (prefix_sums[j] + modulo - k) % modulo
        # This is something I don't even understand how to prove myself... I really wish
        # I took a Number's Theory course back in college!
        # Without 'modulo' part of this problem, this problem would be a trivial
        # "at least k" - "at least k+1" sliding window solution :)

        prefix_map = defaultdict(list)
        for i in range(N):
            prefix_map[(prefix_sums[i - 1] if i - 1 >= 0 else 0) % modulo].append(i)
        
        res = 0
        for r in range(N):
            # Find how many indices l <= r exist such that nums[l..r] is interesting
            # If nums[l..r] is interesting, this implies that:
            #     prefix_sums[r] - (prefix_sums[l - 1] if l - 1 >= 0 else 0) % modulo == k
            # <-> (prefix_sums[l - 1] if l - 1 >= 0 else 0) == (prefix_sums[r] + modulo - k) % modulo
            wanted_sum = (prefix_sums[r] + modulo - k) % modulo

            # res += len(list(filter(lambda index: index <= r, prefix_map[wanted_sum]))) # TOO SLOW!
            arr = prefix_map[wanted_sum]
            # Find rightmost 'rightmost' index in arr such that rightmost <= r
            left, right = 0, len(arr) - 1
            rightmost = None
            while left <= right:
                mid = (left + right) // 2
                index = arr[mid]
                if index <= r:
                    # Valid, look for even 'right-more' indices
                    rightmost = mid
                    left = mid + 1
                else:
                    # Invalid, look to indices on the left
                    right = mid - 1
            
            if rightmost is not None:
                res += rightmost + 1

        return res
