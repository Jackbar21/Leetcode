class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # self.s, self.k = s, k
        # d = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
        # for letter in s:
        #     d[letter] += 1
        # self.memo = {}
        # # return self.dp(d) >= k
        # self.dp(d)
        # return k in self.memo.values()

        d = {letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"}
        for letter in s:
            d[letter] += 1
        
        return len(s) >= k and sum(val % 2 for val in d.values()) <= k

        # In order to split of a section to be palindrome, can only do so
        # if frequency of each letter is even or at MOST ONE letter has odd frequency

        # Idea: Create a collection of k buckets. For each bucket, you will have a frequency
        # dict of letters to letter-frequency, and you can only tolerate AT MOST ONE letter
        # having an ODD frequency (to always keep it a palindrome!)
        self.buckets = [{letter: 0 for letter in "abcdefghijklmnopqrstuvwxyz"} for _ in range(k)]

        self.available_buckets = k

        # The point is to always use up an index i in the bucket, until a decision is made to give
        # it an odd 

        # If anything, we want to pass k denoting "k available buckets to have an odd-level
        # frequency letter" inside of. In each DP call, we will give ourselves a choice of
        # putting a frequency 2 character into a bucket, or a frequency 1 character, for which
        # we must USE UP A NEW BUCKET FOR!!!


    
    def dp(self, d):
        key = tuple(d[letter] for letter in d)
        if key in self.memo:
            return self.memo[key]
        
        if sum(d.values()) <= 1:
            return 1

        count = 0
        d_copy = d.copy()
        for letter, freq in d_copy.items():
            if freq == 0:
                continue
            
            d[letter] -= 2
            count += self.dp(d)
            d[letter] += 2
        
        self.memo[key] = count
        return count


