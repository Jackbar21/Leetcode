class Solution:
    def repeatLimitedStringOld(self, s: str, repeatLimit: int) -> str:
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

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        
        max_heap = [] # (-ord(letter), letter, count) --> first item used for comparisons!
        for letter, count in d.items():
            heapq.heappush(max_heap, (-ord(letter), letter, count))
        
        res = []
        while len(max_heap) > 0:
            comp_val, letter, count = heapq.heappop(max_heap)
            add_count = min(count, repeatLimit)
            res.append(letter * add_count)
            count -= add_count
            if count == 0:
                continue # No more of that letter, so no need to fret about repeatLimit!

            # Now need to add next largest letter. If none, then break!
            if len(max_heap) == 0:
                break
            
            other_comp_val, other_letter, other_count = heapq.heappop(max_heap)
            res.append(other_letter)
            other_count -= 1

            # Add letters back into heap with new counts!
            assert count > 0
            heapq.heappush(max_heap, (comp_val, letter, count))
            if other_count > 0:
                heapq.heappush(max_heap, (other_comp_val, other_letter, other_count))

        
        print(f"{res=}")
        return "".join(res)