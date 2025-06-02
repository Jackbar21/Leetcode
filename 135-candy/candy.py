class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)

        memo = [-1] * N
        def dp(index):
            if memo[index] != -1:
                return memo[index]

            # Neighbors will be adjacent indices of node whose ratings are SMALLER.
            # Since if a neighbor's rating is smaller, that means node at current
            # index needs MORE candy than them. So we'll look at both adjacent neighbors,
            # compute how many candies they need recursively if their rating(s) are smaller,
            # and take 1 more than them to satisfy the condition (but use as few candies
            # as possible!) Of course, if our rating is not larger, than we do not consider
            # these neighbor(s).
            rating = ratings[index]

            # Number of candy child at index i needs. 
            # Must be at least 1 to satisfy first condition!
            res = 1

            # Case 1: Left neighbor
            if index > 0 and ratings[index - 1] < rating:
                case1 = 1 + dp(index - 1)
                # if res < case1:
                #     res = case1
                res = case1
            
            # Case 2: Right neighbor
            if index + 1 < N and ratings[index + 1] < rating:
                case2 = 1 + dp(index + 1)
                if res < case2:
                    res = case2

            memo[index] = res
            return res
        
        return sum(dp(i) for i in range(N))