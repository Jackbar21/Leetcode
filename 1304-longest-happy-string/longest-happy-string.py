class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = []
        d = {'a': a, 'b': b, 'c': c}
        second_last, last = None, None

        while sum(d.values()) > 0:
            options = sorted([letter for letter in 'abc' if not (second_last == last == letter) and d[letter] > 0], key=lambda letter: d[letter])
            if len(options) == 0:
                break
            letter = options[-1]
            # assert d[letter] >= 1
            d[letter] -= 1
            arr.append(letter)

            # Update last letters
            second_last = last
            last = letter

        return ''.join(arr)