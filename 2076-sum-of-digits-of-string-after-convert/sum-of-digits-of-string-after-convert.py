class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        d = {letters[i]: (i+1) for i in range(26)} # letter-to-value map
        transformed_s = ''.join(str(d[letter]) for letter in s)

        # Transform (up to) k times
        for _ in range(k):
            # If transformed string is only one character long, it doesn't matter
            # how many more times we transform it, it will always remain the same.
            if len(transformed_s) == 1:
                break

            transformed_s = str(sum(int(i) for i in transformed_s))

        return int(transformed_s)
