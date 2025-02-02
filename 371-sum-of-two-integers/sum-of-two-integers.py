class Solution:
    def neetcode(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFF

        for i in range(12):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res |= (1 << i)

        if res > 0x7FF:
            res = ~(res ^ mask)
            
        return res
    def getSum(self, a: int, b: int) -> int:
        # return sum([a,b])
        return self.neetcode(a, b)

        self.ignore_first_bit = False
        def numToBinaryString(num):
            binary = bin(num)
            return binary[(2 + (binary[0] == "-")):]
            if binary[0] != "-":
                return "".join(["0", binary[2:]])
            
            # Apply two's complement (flip all the bits, and then add one?)
            self.ignore_first_bit = True
            res = collections.deque(["1" if bit == "0" else "0" for bit in binary]) # Flipped all bits!
            # res = collections.deque(bit for bit in binary)
            for _ in range(3):
                res.popleft() # Get rid of "-0b" prefix!
            res.appendleft("0") # because of two's complement!
            
            # Now add 1!
            for i in range(len(res) - 1, -1, -1):
                if res[i] == "0":
                    res[i] = "1"
                    return "".join(res)
                res[i] = "0" # carry on over to next bit!
            
            res.appendleft("1")
            # return "".join("1" if bit == "0" else "0" for bit in res)
            return "".join(res)

        # return sum([a, b]) # <--- technically valid solution!!!
        # a, b = bin(a)[2:][::-1], bin(b)[2:][::-1]
        # a, b = bin(a), bin(b)
        a, b = numToBinaryString(a), numToBinaryString(b)
        print(f"{a=}, {b=}")
        a, b = a[::-1], b[::-1]
        # return 1
        carry = 0
        
        length = max(len(a), len(b))
        reversed_bits = []
        for i in range(length):
            a_bit = int(a[i]) if i < len(a) else 0
            b_bit = int(b[i]) if i < len(b) else 0

            # Idea: Treat this like kindergarten addition where you go from digits
            # on the right, to digits on the left, and always remembering your carry!
            reversed_bits.append(str(carry ^ a_bit ^ b_bit))
            carry = (carry & a_bit) | (carry & b_bit) | (a_bit & b_bit)

        reversed_bits.append(str(carry))
        bits = collections.deque(reversed(reversed_bits))
        return int("".join(bits), 2)
        while bits[0] == "0":
            bits.popleft()
        if self.ignore_first_bit:
            bits.popleft()
        print(f"{bits=}")

        res = int("".join(bits), 2)
        return res




        # for i in range(min(len(a), len(b))):


        # 1
        # 1
        # _
        # 0

        # 1
        # 19
        # 43
        # __
        #  2

        # 10
        # 01
        # __

        # 5 == 101
        #  --> 011 --> 3