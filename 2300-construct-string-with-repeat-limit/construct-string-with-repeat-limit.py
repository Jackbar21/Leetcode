class Solution:
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
            add_count = count
            if add_count > repeatLimit:
                add_count = repeatLimit
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
            heapq.heappush(max_heap, (comp_val, letter, count))
            if other_count > 0:
                heapq.heappush(max_heap, (other_comp_val, other_letter, other_count))

        return "".join(res)
