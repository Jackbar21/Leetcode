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
                
                return (letter, min(d[letter], repeatLimit))
            
            return (None, 0)

        res = ['']
        cur_streak = 0
        while True:
            if cur_streak < repeatLimit:
                letter, count = getLargestNonEqualLetter(None) # None since no constraint :)
                if letter is None:
                    break
                # if letter is None or count == 0:
                #     assert letter is None and count == 0
                #     break
                if letter == res[-1]:
                    # If we're gonna continue the streak, augment it!
                    count = min(count, repeatLimit - cur_streak)
                    cur_streak += count
                else:
                    # Otherwise, reset it!
                    cur_streak = count

                for _ in range(count):
                    res.append(letter)
                d[letter] -= count
                continue
            
            assert cur_streak == repeatLimit
            letter, count = getLargestNonEqualLetter(res[-1])
            if letter is None:
                break
            res.append(letter)
            d[letter] -= 1
            cur_streak = 1
            continue
        
        return "".join(res)

        terminate = False
        cur_banned = None
        while sum(d.values()) > 0:
            print(f"{d=}")
            # Fill in res with at most 'repeatLimit' of largest character in s
            letter, count = getLargestNonEqualLetter('zz') # 'zz' since 'zz' > 'z'
            print(f"{letter, count=}")
            if letter is None or count == 0:
                assert letter is None and count == 0
                break
            for _ in range(count):
                res.append(letter)
            d[letter] -= count
            
            # Now add exactly one of next largest character, if possible, to satisfy repeatLimit
            # constraint for previously larger letter (in case we still have more of it!)
            other_letter, other_count = getLargestNonEqualLetter(letter)
            print(f"{other_letter, other_count=}")
            if other_letter is None or other_count == 0:
                assert other_letter is None and other_count == 0
                break
            # Only add this once, not count many times!
            res.append(other_letter)
            d[other_letter] -= 1
            continue

            if cur_banned == None:
                for letter in alphabet_backwards:
                    if d[letter] == 0 or letter == cur_banned:
                        continue

                    assert d[letter] > 0
                    repeat_count = min(d[letter], repeatLimit)
                    d[letter] -= repeat_count
                    for _ in range(repeat_count):
                        res.append(letter)
                    cur_banned = letter
                    found_letter = True
                    break
                if not found_letter:
                    break
            
            else:
                for letter in alphabet_backwards:
                    if d[letter] == 0 or letter == cur_banned:
                        continue

                    assert d[letter] > 0
                    res.append(letter)
                    d[letter] -= 1
                    cur_banned = None if repeatLimit > 1 else letter
            continue
                    
                # Now, we must grab the next largest letter and append exactly one of it
                # If none is found, we must terminate the program.
                # did_operation = False
                # for other_letter in alphabet_backwards:
                #     if not (other_letter) < letter:
                #         continue
                    
                #     if d[letter] == 0:
                #         continue

                #     d[letter] -= 1
                #     res.append(letter)
                #     did_operation = True
                #     break
                # if not did_operation:
                #     terminate = True
            # if not did_operation:
            #     break
        
        print(f"{d=}")
        return "".join(res)