class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {}
        for i in range(len(arr)):
            # arr[i] %= k
            d[arr[i] % k] = d.get(arr[i] % k, 0) + 1
        
        # First step: check 0s (i.e. numbers who are direct multiples of k)
        if 0 in d:
            if d[0] % 2 != 0:
                return False
            del d[0]

        # The keys in d represent the value of a for each index i in arr,
        # where arr[i] == a + b * k, for some non-negative integers a, b.
        # So now, as you can imagine, we want to match each key "key1" in d with
        # another key "key2" in d (if available) such that key1 + key2 == k.
        # In other words, in a spirit similar to a problem like Two Sum,
        # given key1, want to find "key2" such that key2 == k - key1.
        # A key like key2 is available if and only if key2's value in d
        # is greater than 0.
        # for key in d:
        for key in range(1, k // 2 + 1):
            if d.get(key, 0) != d.get(k - key, 0):
                return False
        
        return True


            


        

        # arr.sort()
        print(d)
        return False

        # For all i, arr[i] == a + b * k, for some numbers a, b
        # Since the b part doesn't matter, the only "unique" values
        # that remain are for 0 <= a < k

        # (a, b)
        # (a, b, c, d)
        # (a, b) --> solution no longer possible with rest of elements
        # k=5, a=1, b=4, c=9, 
