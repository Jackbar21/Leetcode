class Solution:
    def __init__(self):
        self.nums = None # hash set for O(1) lookup times & no duplicates
        self.memo = {} # num to length of chain from num mappings

    def getChainLength(self, num):
        if num in self.memo:
            return self.memo[num]
        
        # Base Case: num is LAST number in the chain
        if (num + 1) not in self.nums:
            self.memo[num] = 1
            return 1
        
        chain_length = 1 + self.getChainLength(num + 1)
        self.memo[num] = chain_length
        return chain_length
        

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # Get rid of all duplicates in O(n) time
        # Also allows for O(1) lookup times :)
        self.nums = set(nums)

        # Idea: for each number, if we try to compute its chain length (i.e. longest
        # consecutive number of elements chain starting from that number), we can keep
        # checking if next number exist in nums by leveraging O(1) lookup times in hash-set.
        # Then, whenever we're computing the "chain length" from any particular number, we
        # will cache the result to be used whenever needed again in the future. In the worst
        # case, we will store the longest chain for EVERY unique number in nums, which will
        # require a total of O(n) space.
        # As for time complexity, this means that we will only forcibly compute the chain for
        # each number once, and "knock out" any numbers alongside the chain WITH it. This means
        # that each number will have its chain calculated at most once, and from then on their
        # chain be an O(1)-lookup-able value, for a total running time complexity of O(n) [since
        # again, only ONCE will each number be considered.]
        return max(
            self.getChainLength(unique_num)
            for unique_num in self.nums
        )