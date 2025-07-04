class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # First, compute number of times needed to double string such that
        # k'th character actually exists
        num_ops = math.ceil(math.log(k, 2))

        # Firstly, convert k into index form (i.e. subtract 1)
        k -= 1

        # If k == 0, return "a". 
        if k == 0:
            return "a"
        
        operations = operations[:num_ops] # skip first op

        half_len = pow(2, num_ops - 1)
        change_count = 0
        while operations:
            operation = operations.pop()
            k_second_half = k >= half_len
            if operation == 1 and k_second_half:
                change_count += 1

            # Loop Invariant
            k = (k - half_len) if k_second_half else k
            half_len //= 2
        
        return chr(ord("a") + (change_count % 26))
