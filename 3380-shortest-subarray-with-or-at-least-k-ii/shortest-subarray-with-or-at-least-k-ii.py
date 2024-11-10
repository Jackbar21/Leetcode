class Solution:
    def getNum(self, d):
        # Keys are significant bits, values are count of significant bits
        # Hence for each key, if significant bit count >= 1, we add it to result
        res = 0
        for power, count in d.items():
            if count >= 1:
                res += pow(2, power)
        return res
    
    def addNum(self, d, num):
        bin_num = bin(num)[2:]
        for i in range(len(bin_num)):
            if bin_num[-1 - i] == '1':
                d[i] += 1
        
        return d

    def delNum(self, d, num):
        bin_num = bin(num)[2:]
        for i in range(len(bin_num)):
            if bin_num[-1 - i] == '1':
                d[i] -= 1
                if d[i] <= 0:
                    del d[i]
        
        return d

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        res = float("inf")

        l = 0
        for r in range(len(nums)):
            d = self.addNum(d, nums[r])
            while l <= r and self.getNum(d) >= k:
                res = min(res, r - l + 1)
                if l == r:
                    return 1
                
                # Loop Invariant
                d = self.delNum(d, nums[l])
                l += 1

        # Check if no solution
        if res == float("inf"):
            return -1

        return res
