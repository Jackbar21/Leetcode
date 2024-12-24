class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def isPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def checkAllPalindromes(pairs) -> bool:
            for l, r in pairs:
                if not isPalindrome(l, r):
                    return False
            return True

        partitions = []
        res = set()
        def backtrack(i):
            # Base Case: If i >= len(s), then we want to check if every partition
            # is a palindrome!
            if i >= len(s):
                string_pairs = []
                l = 0
                for r in partitions:
                    string_pairs.append((l, r))
                    l = r + 1
                # last_string = s[l:]
                # if last_string != "":
                #     strings.append(last_string)
                if l < len(s):
                    string_pairs.append((l, len(s) - 1))
                # pairs.append(l, len(s) - 1)

                # strings = ["".join(partition) for partition in partitions]
                if checkAllPalindromes(string_pairs):
                    res.add(tuple(string_pairs))
                return

            letter = s[i]

            # Case 1: make a partition at index i
            partitions.append(i)
            backtrack(i + 1)
            partitions.pop()

            # Case 2: Don't make a partition at index i
            backtrack(i + 1)

            return

            # Case 1: add letter at index i into last partition
            # (Can only do this if I have at least one partition in the first place!)
            if len(partitions) > 0:
                partitions[-1].append(letter)
                backtrack(i + 1)
                partitions[-1].pop()

            # Case 2: add letter at index i into new partition
            partitions.append([letter])
            backtrack(i + 1)
            partitions.pop()
        
        backtrack(0)
        return list([[s[i:j+1] for i,j in pairs] for pairs in res])