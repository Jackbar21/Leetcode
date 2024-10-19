class Solution:
    # Returns 0 or 1, as int.
    def findKthBitHelper(self, k, max_val):
        if max_val <= 1:
            # assert max_val == 1
            return 0

        mid = max_val // 2

        if k <= mid:
            return self.findKthBitHelper(k, mid)
        
        if k == mid + 1:
            return 1
        
        new_k = max_val - k + 1
        return 1 - self.findKthBitHelper(new_k, mid)

    def findKthBit(self, n: int, k: int) -> str:
        max_val = pow(2, n) - 1
        return str(self.findKthBitHelper(k, max_val))