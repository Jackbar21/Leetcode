class Solution:
    def __init__(self):
        self.k = None
        self.nums = None
        self.memo = {}

    def minSubarrayDp(self, i, bitwise_or):
        if i >= len(self.nums):
            return 0 if bitwise_or >= self.k else float("inf")
        
        if (i, bitwise_or) in self.memo:
            return self.memo[(i, bitwise_or)]
        
        # Case 1: Include num at index i
        case1 = 1 + self.minSubarrayDp(i + 1, bitwise_or | self.nums[i])

        # Case 2: Don't include num at index i
        case2 = self.minSubarrayDp(i + 1, bitwise_or)

        res = min(case1, case2)
        self.memo[(i, bitwise_or)] = res
        return res

    def getNum(self, d):
        # Keys are significant bits, values are count of significant bits
        # Hence for each key, it'll be value * 2^key
        res = 0
        for power, count in d.items():
            # assert count >= 0 and power >= 0
            # res += count * pow(2, power)
            if count >= 1:
                res += pow(2, power)
        return res
    
    def addNum(self, d, num):
        bin_num = (bin(num)[2:])[::-1]
        for i in range(len(bin_num)):
            if bin_num[i] == '1':
                d[i] += 1
        
        return d

    def delNum(self, d, num):
        bin_num = (bin(num)[2:])[::-1]
        for i in range(len(bin_num)):
            if bin_num[i] == '1':
                d[i] -= 1
                assert d[i] >= 0
        
        return d

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # First, check if there is NO solution
        bitwise_or = 0
        for num in nums:
            bitwise_or |= num
        if bitwise_or < k:
            return -1


        self.nums = nums
        self.k = k
        # return self.minSubarrayDp(0, 0)

        # d = {} # key = sig. bit, val = # of such sig. bits
        d = defaultdict(int)
        l = 0
        res = float("inf")
        bitwise_or = 0
        for r in range(len(nums)):
            # if l == r == 4:
                # print("MAS")
                # print(d)
            d = self.addNum(d, nums[r])
            while l <= r and self.getNum(d) >= k:
                # if l == r == 4:
                    # print("MAS")
                    # print(d)
                # if l == r:
                #     break
                res = min(res, r - l + 1)
                
                if r - l + 1 < 3:
                    print(l, r, self.getNum(d), k, d)
                new_d = defaultdict(int)
                new_d = self.addNum(new_d, 95)
                new_d = self.addNum(new_d, 67)
                print(new_d)
                # # print(l, r, r - l + 1)
                # print(d)
                prev = self.getNum(d)
                d = self.delNum(d, nums[l])
                new = self.getNum(d)
                assert prev >= new
                l += 1
        
        # while l < len(nums) and self.getNum(d) >= k:
        #     res = min(res, len(nums) - l)
        #     d = self.delNum(d, nums[l])
        #     l += 1

        # print(l)


        return -1 if res == float("inf") else res

        

        # Get all bitwise ors starting from index i
        # get all bitwise ors ending at index i

        nums.sort(reverse=True)
        bitwise_or = 0
        count = 0
        for num in nums:
            if bitwise_or >= k:
                return count

            # Loop Invariant
            new_bitwise_or = bitwise_or | num
            if new_bitwise_or > bitwise_or:
                bitwise_or = new_bitwise_or
                count += 1
            
        return -1

        # 1011000101
        # 1000000000


        
