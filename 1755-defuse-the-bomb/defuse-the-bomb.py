class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        
        return self.decryptPos(code, k) if k > 0 else self.decryptNeg(code, -k)
    
    def decryptPos(self, code, k):
        new_code = []
        cur_sum = 0
        for i in range(k):
            index = i % len(code)
            cur_sum += code[i]

        l, r = 0, ((k - 1) % len(code))

        for i in range(len(code)):
            # Update cur_sum
            cur_sum -= code[l]
            l += 1
            l %= len(code)

            r += 1
            r %= len(code)
            cur_sum += code[r]

            # Modify with new value at index i
            new_code.append(cur_sum)

        return new_code
    
    def decryptNeg(self, code, k):
        new_code = []
        cur_sum = 0
        index = -1
        for i in range(k):
            index = (len(code) - 1) - (i % len(code))
            cur_sum += code[index]

        l, r = index, len(code) - 1

        for i in range(len(code)):
            # Modify with new value at index i
            new_code.append(cur_sum)
            
            # Update cur_sum
            cur_sum -= code[l]
            l += 1
            l %= len(code)

            r += 1
            r %= len(code)
            cur_sum += code[r]   

        return new_code
