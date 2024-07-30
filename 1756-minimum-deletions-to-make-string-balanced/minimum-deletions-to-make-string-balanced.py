class Solution:
    # s = (a+b)*
    # want s to be: a*b*
    def __init__(self):
        # self.memo = {-1: 0}
        # self.memo = {}
        self.memo = {0: (0, 0)}
    
    def minimumDeletionsDp2(self, s, i):
        if i in self.memo:
            return self.memo[i]
        
        # self.memo[i-1] = (del_a, del_b)
        del_a, del_b = self.minimumDeletionsDp2(s, i - 1)

        # if s[i] == 'a':
            # 1. keep a



        # return self.memo[i]

    def minimumDeletionsDp(self, s, i):
        if i in self.memo:
            return self.memo[i]
        
        # Logic here
        # we have access to self.memo[i-1], which is
        # optimal (k, num_ending_bs) sol. for s[:i] (not including i)
        k, num_ending_bs = self.minimumDeletionsDp(s, i - 1)

        # Want to find optimal solution for s[:i+1] (not including i+1)
        # Case 1: s[i] == 'a'
        if s[i] == 'a':
            num_beginning_as = i - num_ending_bs

            # keep 'a'
            # (i) no previous b's, so nothing
            # (ii) X previous b's, gotta delete them

            # Case (a): delete 'a'
            case1 = (k + 1, num_ending_bs)
            # Case (b): delete ALL previous b's
            case2 = (k + num_ending_bs, 0)
            # TODO: verify what you want if == case, likely case2
            # since smaller num_ending_bs == more flexibility?
            self.memo[i] = case1 if case1[0] < case2[0] else case2

        # Case 2: s[i] == 'b'
        else:
            assert s[i] == 'b'
            # Case (a): keep 'b'
            case1 = (k, num_ending_bs + 1)
            # Case (b): delete 'b'
            case2 = (k + 1, num_ending_bs)
            # TODO: What I'm realizing, is that case1 will always win
            # Idea behind it: why delete a b if you don't have to?
            self.memo[i] = case1 if case1[0] < case2[0] else case2
        
        assert i in self.memo
        return self.memo[i]
    def minimumDeletions(self, s: str) -> int:
        num_b_before, num_a_after = 0,0
        for c in s:
            if c == 'a':
                num_a_after += 1
        
        min_deletions = num_a_after
        if s[0] == 'a':
            min_deletions -= 1

        for i in range(len(s)):
            if s[i] == 'b':
                num_b_before += 1
            else:
                num_a_after -= 1
            
            deletions_needed = num_b_before + num_a_after
            
            min_deletions = min(min_deletions, deletions_needed)

        return min_deletions

        for i in range(len(s)):
            num_b_before = 0
            for j in range(i):
                if s[j] == 'b':
                    num_b_before += 1
            
            num_a_after = 0
            for j in range(i+1, len(s)):
                if s[j] == 'a':
                    num_a_after += 1
            
            # self.memo[i] = 
            deletions = num_b_before + num_a_after
            min_deletions = min(min_deletions, deletions)
        return min_deletions

        # minimum number of deletions upto s[:i-1]
        # want: upto s[:i]
        self.memo[0] = (0,0) if s[0] == 'a' else (0,1)
        res = self.minimumDeletionsDp(s, len(s)-1)[0]
        print(self.memo)
        return res

        # s[:i-1] == self.memo[i-1] == (k, num_ending_bs)
        # Case 1: s[i] == 'a'
        #     Case (a): delete 'a'
        #               k += 1
        #     Case (b): delete ALL previous b's
        #               k += num_ending_bs
        #               num_ending_bs = 0
        #     self.memo[i] = (k, num_ending_bs)

        # s[:i-1] == self.memo[i-1] == (k, num_ending_bs)
        # Case 2: s[i] == 'b'
        #         Case (a): keep 'b'
        #                   num_ending_bs += 1
        #         Case (b): delete 'b'
        #                   k += 1
        #     self.memo[i] = (k, num_ending_bs)

        # Case 2: s[i] == 'b'