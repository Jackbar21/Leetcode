class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # Firstly, convert k into index form (i.e. subtract 1)
        k -= 1

        # If k == 0, return "a". 
        if k == 0:
            return "a"
        
        # Otherwise, assume starting at "aa" or "ab" depending on operations[0],
        # so that length of string is thus ALWAYS EVEN.
        base_string = "aa" if operations[0] == 0 else "ab"

        num_ops = math.ceil(math.log(k + 1, 2))
        print(f"{num_ops=}, {pow(2, num_ops - 1)=}, {k=}, {pow(2, num_ops)=}")
        operations = operations[:num_ops] # skip first op

        word_len = pow(2, num_ops)
        print(f"{word_len=}")
        change_count = 0
        while len(operations) > 0:
            operation = operations.pop()
            half_len = word_len // 2
            print(f"{k=}, {half_len=}, {word_len=}, {operation=}")
            if operation == 1 and k >= half_len:
                change_count += 1
            prev_index = (k - half_len) if k >= half_len else k
            print(f"{k=}, {prev_index=}, {change_count=}")
            print()

            # Loop Invariant
            k = prev_index
            word_len //= 2
        
        print(f"{change_count=}")
        return chr(ord("a") + (change_count % 26))



        print(f"{math.log(k, 2)=}")

        getNextLetter = lambda letter: "a" if letter == "z" else chr(ord(letter) + 1)
        
        word = "a"

        operation_index = 0
        while len(word) < k:
            operation = operations[operation_index]
            append_string = word if operation == 0 else "".join(map(getNextLetter, word))
            word += append_string

            # Loop Invariant
            operation_index += 1

        return word[k - 1]

# a                 0
# a|b               1
# ab|bc             3
# abbc|bccd         3
# abbcbccd|bccdcdde 11

# If k == 1, return "a". Otherwise, assume starting at "aa" or "ab" depending on operations[0],
# so that length of string is thus ALWAYS EVEN.