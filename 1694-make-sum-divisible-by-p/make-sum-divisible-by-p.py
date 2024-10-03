class Solution:
    def __init__(self):
        self.nums = None
        self.p = None
        self.memo = {}
        self.prefix = [] # prefix[i] == sum of nums[:i]
        self.sum_nums = 0
        self.target = 0
    
    # Returns sum(self.nums) - sum(self.nums[i: j + 1])
    def getDiffSum(self, i, j):
        # TODO: remove for efficiency sake
        return sum(self.nums) - sum(self.nums[i: j + 1])
        prefix_i = prefix[i - 1] if i > 0 else 0
        prefix_j = prefix[j + 1] if j + 1 < len(nums) else sum_nums
        return sum_nums + prefix[i - 1] - prefix[j + 1]
    
    def getSubarraySum(self, i, j):
        prefix_i = self.prefix[i - 1] if i > 0 else 0
        return self.prefix[j] - prefix_i
    def minSubarray(self, nums: List[int], p: int) -> int:
        # nums.sort()
        # Idea: removing fewest amount of numbers <==> keeping largest amount of numbers
        # l = 0, r = len(nums) - 1
        # (i, j), 0 <= i,j < len(nums)
        self.nums = nums
        self.p = p
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            cur_sum %= p
            self.prefix.append(cur_sum)
        # prefix = self.prefix
        self.sum_nums = cur_sum
        prefix = self.prefix

        remainder = self.sum_nums % p
        if remainder == 0:
            return 0
        # self.target = remainder

        # Couldn't solve it on my own - had to look at editorial.
        # This was a really difficult problem from this point on.
        res = len(nums)
        seen = {0: -1} # 0 case ripped straight from Editorial
        for i in range(len(nums)):
            cur_sum = prefix[i]
            needed = (cur_sum - remainder + p) % p # Ripped straight from Editorial
            if needed in seen:
                res = min(res, i - seen[needed])
            
            # Even if cur_sum in seen, update it again such that next use case
            # will be with larger i, and hence the smaller possible/available
            # subarray to remove
            seen[cur_sum] = i
        
        return res if res < len(nums) else -1
        # Noor idea:
        # Go through each i. Then get sum of nums[:i]. Now figure
        # out smallest j>=i such that, (sum(nums[:i]) + sum(nums[j:])) % p == 0.
        # already know sum(nums[:i]) == prefix[i - 1]
        # sum(nums[j:]) == prefix[len(nums) - 1] - prefix[j]
        max_heap = []
        for i in range(len(nums)):
            prefix_i = prefix[i - 1] if i > 0 else 0
            sum_nums = prefix[len(nums) - 1]
            j = i + 1
            while j < len(nums):
                if (prefix_i + (sum_nums - prefix[j])) % p == 0:
                    heapq.heappush(max_heap, ((j - i + 1), i, j))
                    break
                j += 1
        print(max_heap)
        return 1
                
            
    
    # Return smallest subarray with value == to target
    def subsetSumDp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if self.getSubarraySum(i, j) == self.target:
            self.memo[(i, j)] = True
            return True
        


        
        # Want subarray (i, j) whose remainder == 'remainder'.
        # I.e. sum(nums[i: j + 1]) % p == remainder
        # <--> (prefix[j+1] - prefix[i-1]) % p == remainder
        # <--> prefix[j+1]%p - prefix[i-1]%p == remainder
        
        # i, j = 0,len(nums) - 1
        # res = (0, len(nums) - 1)
        # while 0 <= i < len(nums) and 0 <= j < len(nums):
        #     sub_sum = self.getSubarraySum(i, j)
        #     print(i, j, sub_sum)
        #     if sub_sum > remainder:
        #         i += 1
        #     elif sub_sum < remainder:
        #         j -= 1
        #     else:
        #         # cur_len = res[1] - res[0] + 1
        #         # if cur_len > j - i + 1:
        #         #     res = (i, j)
        #         return j - i + 1
        #         # i += 1
        # return -1
        # if res == (0, len(nums) - 1):
        #     return -1
        # i, j = res
        # return j - i + 1

        
        # Idea: want to remove smallest subarray whose sum also has a remainder
        # of value 'remainder'

        # want (prefix[j] - prefix[i-1]) == remainder

        # Noor idea:
        # Go through each i. Then get sum of nums[:i]. Now figure
        # out smallest j such that, (sum(nums[:i]) + sum(nums[j+1:])) % p == 0.
        # already know sum(nums[:i]) == prefix[i - 1]
        # sum(nums[j+1:]) == prefix[len(nums) - 1] - prefix[j + 1]
        for i in range(len(nums)):
            prefix_i = prefix[i - 1] if i > 0 else 0

            


        # Core Idea:
        # If I remove subarray (i, j) from nums then I'm left with:
        # sum(nums) - sum(nums[i:j + 1])
        # <--> sum(nums[:i]) + sum(nums[j+1:])
        # <--> prefix[i - 1] + (sum(nums) - prefix[j + 1])
        # sum(nums) + prefix[i - 1] - prefix[j + 1]
        # IDEA TO CONSIDER: Modulo the prefix sum values by p (Be careful - might lose data)
        print(self.prefix)
        print(self.sum_nums)
        return 1
        
        res = self.minSubarrayDp(0, len(nums) - 1)
        print(res)
        return len(nums) - res[0]
        print(self.prefix)
        return self.prefix[2] - self.prefix[1]
    
    def minSubarrayDp(self, i, j):
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if i > j:
            return (0, i, j)
        
        diff = self.prefix[i - 1] if i > 0 else 0
        sub_sum = self.prefix[j] - diff

        if sub_sum % self.p == 0:
            self.memo[(i, j)] = (j - i + 1, i, j)
            return self.memo[(i, j)]

        # Case 1: move left pointer (i.e. i++)
        case1 = self.minSubarrayDp(i + 1, j)

        # Case 2: move right pointer (i.e. j--)
        case2 = self.minSubarrayDp(i, j - 1)

        res = case2
        if case1[0] > case2[0]:
            res = case1
        
        self.memo[(i, j)] = res
        return res
