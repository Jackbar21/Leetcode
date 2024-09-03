class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # In case you guys don't hear me well, I'll make sure
        # to write out my steps & ideas as I go along. I'm currently
        # on the train back to Seattle from my mini-trip to Vancouver :)

        # Step 1: Convert the string 's' into the number
        # First thing we need is a hashmap
        letters = 'abcdefghijklmnopqrstuvwxyz'
        d = {letters[i]: (i+1) for i in range(26)} # letter to value mappings
        transformed_s = ''.join(str(d[letter]) for letter in s)

        # Transform up to k times (exit early if digit is 1 character long, since
        # 8 --> 8 --> 8 .... --> 8 no matter how many times you repeat, and same for 1-9)
        for _ in range(k):
            if len(transformed_s) <= 1:
                assert len(transformed_s) == 1
                break
            
            transformed_s = str(sum(int(i) for i in transformed_s))

        return int(transformed_s)
