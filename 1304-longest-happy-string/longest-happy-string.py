class Solution:
    def getNextLetter(self, d, banned):
        options = [letter for letter in 'abc' if letter != banned and d[letter] > 0]
        # d = {'a': a, 'b': b, 'c': c}
        options.sort(key = lambda letter: d[letter], reverse=True) # O(1)
        print(f"{options[0]=}, {d=}, {banned=}")
        return options[0]

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = []
        banned = None
        d = {
            'a': a,
            'b': b,
            'c': c
        }
        last_letters = collections.deque([None, None])

        while sum(d.values()) > 0:
            # options = [letter for letter in 'abc' if letter != banned]
            # letter = self.getNextLetter(d, banned)

            options = sorted([letter for letter in 'abc' if not (last_letters[0] == last_letters[1] == letter) and d[letter] > 0], key=lambda letter: d[letter], reverse=True)
            if len(options) == 0:
                break
            letter = options[0]
            assert d[letter] >= 1
            d[letter] -= 1
            arr.append(letter)
            # Update last letters
            last_letters.popleft()
            last_letters.append(letter)
            continue
            
            print(f"{options[0]=}, {d=}, {banned=}")
            if d[letter] >= 2:
                d[letter] -= 2
                banned = letter
                arr.append(letter)
                arr.append(letter)
            else:
                print(d, letter)
                assert d[letter] == 1 # since sum of values > 0
                d[letter] = 0
                arr.append(letter)
                banned = letter
        
        return ''.join(arr)


            

        #     # a is the biggest
        #     if a == max(a, b, c) and banned != 'a':
        #         assert a >= 1
        #         arr.append('a')
        #         a -= 1
        #         if a > 0:
        #             arr.append('a')
        #             a -= 1
        #             banned = 'a'
        #     # b is the biggest
        #     elif b == max(a, b, c) and banned != 'b':
        #         assert b > a
        #         assert b >= 1
        #         arr.append('b')
        #         b -= 1
        #         if b > 0:
        #             arr.append('b')
        #             b -= 1
        #             banned = 'b'
        #     # c is the biggest
        #     else:
        #         assert c == max(a, b, c)
        #         assert c >= 1
        #         assert banned != 'c'
        #         arr.append('c')
        #         c -= 1
        #         if c > 0:
        #             arr.append('c')
        #             c -= 1
        #             banned = 'c'
        
        # return ''.join(arr)