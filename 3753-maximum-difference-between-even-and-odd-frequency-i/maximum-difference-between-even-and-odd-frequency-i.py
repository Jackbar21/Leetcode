class Solution:
    def maxDifference(self, s: str) -> int:
        # Since we want to find maximum difference a1 - a2, this means we want to
        # MAXIMIZE the value of a1 and MINIMIZE the value of a2.
        # a1 is for odd frequency characters, so find LARGEST odd frequency
        # a2 is for even frequency characters, so find SMALLEST even frequency

        # Step 1: Get frequency of each character
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        
        a1, a2 = float("-inf"), float("inf")
        for freq in d.values():
            if freq % 2:
                if freq > a1:
                    a1 = freq
            elif freq < a2:
                a2 = freq
        return a1 - a2
        
        # Step 2: Get max odd frequency
        a1 = max(freq for freq in d.values() if freq % 2 == 1)

        # Step 3: Get min even frequency
        a2 = min(freq for freq in d.values() if freq % 2 == 0)

        # Step 4: Return maximum difference
        return a1 - a2
