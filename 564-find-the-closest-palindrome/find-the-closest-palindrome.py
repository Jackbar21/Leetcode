class Solution:
    def large(self, n):
        # Left "includes" mid, regardless of whether n is even or odd
        left = n[:math.ceil(len(n) / 2)]
        right = n[math.ceil(len(n) / 2):]

        # Take a case such as 807045053224792883. When we split it into a left & right
        # substring as per the logic above, we'll have: 
        #       left = 807045053, right = 224792883.
        # Now, the final solution will clearly build around changing the value of right.
        # But in doing so, we might change the least significant digit from the 'left'
        # substring by either -1, 0, or 1. Hence, we need to consider all three cases,
        # and return the best result out of all of them.
        candidates = [int(left) - 1, int(left), int(left) + 1]
        res = [self.largeHelper(f"{l}{right}") for l in candidates]
        res = list(filter(lambda x: x!= self.n, res))
        res.sort(key=lambda x: (abs(int(n) - int(x)), x)) # O(1), only 3 elements
        return res[0] if res[0] != self.n else res[1]
    def largeHelper(self, n):
        # First thing to check is if n is of even or odd length
        # if odd length, we can ignore the digit at dead-center of n,
        # located at index n // 2
        mid = len(n) // 2
        left = n[:mid] if len(n) % 2 == 0 else n[:mid]
        right = n[mid:] if len(n) % 2 == 0 else n[mid + 1:]
        
        # Idea is to make the right substring equivalent to the left
        # substring, but in reverse. This is because changing the numbers
        # on the right is much "cheaper" than in the left. I.e. for a number
        # such as 807045053224792883, to decrement the 8 on the left by one to a 7,
        # you are changing the number by a factor of 100 Quadrillion, whereas if you wanna
        # change the 3 on the right by one to a 2, you are only changing the number by 1.
        # Hence, since we want the closest palindrome, given the definition of distance,
        # it will be much "cheaper" to fit the right substring to be the reverse of the left one.
        diff = abs(int(left[::-1]) - int(right))
        if self.isPalindrome(str(int(n) - diff)):
            return str(int(n) - diff)
        return str(int(n) + diff)
    def nearestPalindromic(self, n: str) -> str:
        self.n = n
        num = int(n)
        if num <= 10:
            return str(num - 1)
        
        if len(n) >= 3:
            return self.large(n)
        
        offset = 1
        while True:
            # Check smaller number first
            if self.isPalindrome(str(num - offset)):
                return str(num - offset)
            
            # Now check larger number
            if self.isPalindrome(str(num + offset)):
                return str(num + offset)
            
            # Loop invariant
            offset += 1
        
        # return self.npHelper(num, 1)
        raise Exception("Not Reachable")

    def isPalindrome(self, n):
        l, r = 0, len(n) - 1
        while l < r:
            if n[l] != n[r]:
                return False
            l += 1
            r -= 1
        return True
