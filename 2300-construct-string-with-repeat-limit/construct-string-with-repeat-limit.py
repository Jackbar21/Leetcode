class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet_backwards = alphabet[::-1]
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        
        def getLargestNonEqualLetter(banned_letter): 
            for letter in alphabet_backwards:
                if letter == banned_letter:
                    continue

                if d[letter] == 0:
                    continue
                
                count = d[letter]
                if repeatLimit < count:
                    count = repeatLimit
                return (letter, count)
            
            return (None, 0)

        res = ['']
        cur_streak = 0
        while True:
            if cur_streak < repeatLimit:
                letter, count = getLargestNonEqualLetter(None) # None since no constraint :)
                if letter is None:
                    break
    
                if letter == res[-1]:
                    # If we're gonna continue the streak, augment it!
                    if repeatLimit - cur_streak < count:
                        count = repeatLimit - cur_streak
                    cur_streak += count
                else:
                    # Otherwise, reset it!
                    cur_streak = count

                for _ in range(count):
                    res.append(letter)
                d[letter] -= count
                continue
            
            # assert cur_streak == repeatLimit
            letter, count = getLargestNonEqualLetter(res[-1])
            if letter is None:
                break
            res.append(letter)
            d[letter] -= 1
            cur_streak = 1
        
        return "".join(res)
