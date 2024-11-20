class Solution:
    # O(1)
    def isValidSubstring(self, i, j):
        # Substring s[i..j] is valid if and only if
        # the number of a's, b's, and c's in this substring
        # are each respectively less than or equal to their
        # maximum thresholds: max_a, max_b, and max_c
        dj = self.prefix[j]
        a, b, c = dj['a'], dj['b'], dj['c']
        if i > 0:
            di = self.prefix[i - 1]
            a -= di['a']
            b -= di['b']
            c -= di['c']
        
        return (a <= self.max_a 
            and b <= self.max_b 
            and c <= self.max_c)

    def takeCharacters(self, s: str, k: int) -> int:
        # No deletions necessary, so return 0!
        if k == 0:
            return 0

        d = {letter: 0 for letter in 'abc'}
        prefix = []

        for letter in s:
            d[letter] += 1
            prefix.append(d.copy())
        
        max_a = s.count('a') - k
        max_b = s.count('b') - k
        max_c = s.count('c') - k
        if max_a < 0 or max_b < 0 or max_c < 0:
            # No possible solution!
            return -1
        if max_a == max_b == max_c == 0:
            # Only possible solution is to take the entire string s!
            return len(s)
        self.max_a, self.max_b, self.max_c = max_a, max_b, max_c

        # We want essentially largest subarray sum (where sum is defined as
        # number of a's + number of b's + number of c's) where the count of
        # each letter is <= their maximum threshold (defined as max_a, max_b, max_c)
        # This is essentially a problem reduction, since we turned the problem from
        # "remove smallest size subarray from length and right such that sum of each
        # letter is at least k" to "obtain largest subarray from middle such that sum
        # of each letter doesn't exceed its total count - k" :)
        self.memo = {}
        self.s = s
        self.prefix = prefix
       
        largest_valid_subarray_length = max(
            self.dp(i)
            for i in range(len(s))
        )
        return len(s) - largest_valid_subarray_length
    
    # Largest valid subarray starting at index i
    def dp(self, i):
        if i in self.memo:
            return self.memo[i]
        
        # if not 0 <= i < len(self.s):
        #     raise Exception("Impossible case!")

        # Binary search accross every possible j, where i < j < len(s)
        # The larger j is, the more a's, b's and c's will be covered,
        # hence the more likely one of the three max_a, max_b, max_c thresholds
        # will become exceeded. Hence, for any INVALID pair (i, j), we know it will
        # also be invalid for any pair (i, k) where j <= k. Conversevely, for any VALID
        # pair (i, j), we know it will also be a valid pair for any pair (i, k) where k <= j.
        # Hence, we can run rightmost-binary search to find the valid pair (i, j) with maximal
        # value j, to obtain the largest valid subarray starting from index i!
        # res = float("-inf")
        l, r = i, len(self.s) - 1 # i + 2 since already checked k == 0 case!
        rightmost_index = -1
        while l <= r:
            mid = (l + r) // 2
            if self.isValidSubstring(i, mid):
                rightmost_index = max(rightmost_index, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        res = -1
        if rightmost_index != -1:
            res = (rightmost_index - i + 1)
        self.memo[i] = res
        return res