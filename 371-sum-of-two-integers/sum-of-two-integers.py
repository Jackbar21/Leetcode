class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFF

        for i in range(12):
            a_bit, b_bit = a & 1, b & 1
            a >>= 1; b >>= 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit & b_bit) | (a_bit & carry) | (b_bit & carry)
            res |= (cur_bit << i)

        # This was thanks to neetcode :)
        if res > 0x7FF:
            res = ~(res ^ mask)
            
        return res