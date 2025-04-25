class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        N = len(nums)
        # print(f"{nums=}")
        # print(f"{list(map(lambda num: num % modulo == k, nums))=}")

        mapped_nums = [num % modulo == k for num in nums]
        prefix_sums = []
        cur_sum = 0
        for boolean in mapped_nums:
            cur_sum += boolean
            prefix_sums.append(cur_sum)
        # print(f"{prefix_sums=}")
        # print(f"{prefix_sums=}")

        is_interesting = lambda i, j: (prefix_sums[j] - (prefix_sums[i - 1] if i - 1 >= 0 else 0)) % modulo == k
        # return sum(is_interesting(i, j) for i in range(N) for j in range(i, N))

        # res = 0
        # for i in range(N):
        #     prefix_i = prefix_sums[i - 1] if i - 1 >= 0 else 0
        #     for j in range(i, N):
        #         cnt = prefix_sums[j] - prefix_i
        #         res += cnt % modulo == k
        # return res

        # Okay at this point -- I got stuck, and chose to look at the hints. Hints 1-4 are useless
        # for me, but Hint #5 denotes something interesting:
        #     prefix_sums[j] - prefix_sums[i - 1] % modulo == k
        # <-> prefix_sums[i - 1] = (prefix_sums[j] + modulo - k) % modulo
        # This is something I don't even understand how to prove myself... I really wish
        # I took a Number's Theory course back in college!
        # Without 'modulo' part of this problem, this problem would be a trivial
        # "at least k" - "at least k+1" sliding window solution :)

        # For each index j, count how many indices i, i <= j, such that nums[i..j] are interesting.
        # If nums[i..j] is interesting, this implies that:
        #     prefix_sums[j] - (prefix_sums[i - 1] if i - 1 >= 0 else 0) % modulo == k
        # <-> (prefix_sums[i - 1] if i - 1 >= 0 else 0) == (prefix_sums[j] + modulo - k) % modulo

        prefix_map = defaultdict(list)
        for i, prefix_sum in enumerate(prefix_sums):
            prefix_map[(prefix_sums[i - 1] if i - 1 >= 0 else 0) % modulo].append(i)
            # prefix_map[prefix_sum].append(i)
        
        # print(f"{prefix_map=}")

        # prefix_map = defaultdict(int)
        # res = 0
        # for j in range(N):
        #     # For each index j, count how many indices i, i < j, where:
        #     #     (prefix_sums[j] - prefix_sums[i]) % modulo == k
        #     # <-> prefix_sums[i] == (prefix_sums[j] + modulo - k) % modulo, BY HINT #5
        #     wanted_sum = (prefix_sums[j] + modulo - k) % modulo
        #     res += prefix_map[prefix_sums[j] % modulo]
        #     prefix_map[wanted_sum] += 1
        # return res

        
        res = 0
        for r in range(N):
            # Find how many indices l <= r exist such that nums[l..r] is interesting
            # If nums[l..r] is interesting, this implies that:
            #     prefix_sums[r] - (prefix_sums[l - 1] if l - 1 >= 0 else 0) % modulo == k
            # <-> (prefix_sums[l - 1] if l - 1 >= 0 else 0) == (prefix_sums[r] + modulo - k) % modulo
            wanted_sum = (prefix_sums[r] + modulo - k) % modulo
            # print(f"{wanted_sum=}")

            # TODO: Binary Search
            # res += len(list(filter(lambda index: index <= r, prefix_map[wanted_sum])))
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



        self.modulo = modulo
        self.k = k
        self.prefix_sums = prefix_sums
        return self.dp(0, 0)
    
    @cache
    def dp(self, i, count):
        modulo, k, prefix_sums = self.modulo, self.k, self.prefix_sums
        N = len(self.prefix_sums)
        res = 0
        if count % modulo == k:
            res += 1
        
        if i >= N:
            return res
        
        # Case 1: Continue subarray from index i
        case1 = 0 if 0 == self.prefix_sums[i] else self.dp(i + 1, count + self.prefix_sums[i])

        # Case 2: Don't continue subarray from index i
        case2 = self.dp(i + 1, 0) if count != 0 else 0

        return case1 + case2

