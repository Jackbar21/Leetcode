class Solution:
    def minDeletions(self, s: str) -> int:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        values = sorted(d.values())

        used = set()
        res = 0
        for val in values:
            while val > 0 and val in used:
                val -= 1
                res += 1
            used.add(val)
        return res

        print(d)
        print(values)
        res = 0
        min_val = 0
        max_val = 0
        used = set()
        for val in values:
            if val not in used:
                used.add(val)
                continue
            # if val > max_val:
            #     max_val = val
            min_val = max_val = val
            while min_val in used:
                min_val -= 1
            while max_val in used:
                max_val += 1
            # Can subtract to min_val, or go to max_val
            diff_min = val - min_val
            diff_max = max_val - val
            assert min_val <= max_val
            assert diff_min >= 0
            assert diff_max >= 0

            print(f"{diff_min=}, {diff_max=}, {min_val=}, {max_val=}, {val=}, {used=}")

            if diff_min <= diff_max:
                res += diff_min
                used.add(min_val)
            else:
                res += diff_max
                used.add(max_val)
        
        return res

            