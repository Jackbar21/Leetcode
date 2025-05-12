class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        N = len(digits)
        res = set()

        is_valid = lambda x, y, z: x != 0 and z % 2 == 0
        get_number = lambda x, y, z: (x * 100) + (y * 10) + z
        
        for i, digit_i in enumerate(digits):
            for j in range(i + 1, N):
                digit_j = digits[j]
                for k in range(j + 1, N):
                    digit_k = digits[k]
                    
                    # Given digit_i, digit_j, digit_k, there are 6 ways
                    # we can rearrange these digits. Append all valid
                    # ways to res
                    for x, y, z in [
                        (digit_i, digit_j, digit_k),
                        (digit_i, digit_k, digit_j),
                        (digit_j, digit_i, digit_k),
                        (digit_k, digit_i, digit_j),
                        (digit_j, digit_k, digit_i),
                        (digit_k, digit_j, digit_i)
                    ]:
                        # if is_valid(x, y, z):
                        #     res.add(get_number(x, y, z))
                        if x != 0 and z % 2 == 0:
                            res.add((x * 100) + (y * 10) + z)
        
        return sorted(res)
