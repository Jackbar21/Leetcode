class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def checkAllPalindromes(strings: List[str]) -> bool:
            for string in strings:
                if not isPalindrome(string):
                    return False
            return True

        partitions = []
        res = set()
        def backtrack(i):
            # Base Case: If i >= len(s), then we want to check if every partition
            # is a palindrome!
            if i >= len(s):
                strings = []
                l = 0
                for r in partitions:
                    strings.append(s[l:r + 1])
                    l = r + 1
                last_string = s[l:]
                if last_string != "":
                    strings.append(last_string)
                # pairs.append(l, len(s) - 1)

                # strings = ["".join(partition) for partition in partitions]
                if checkAllPalindromes(strings):
                    res.add(tuple(strings))
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
        return list(res)