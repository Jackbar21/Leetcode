class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # 1, 2, 3, ..., k-3,k-2,k-1
        # 1,k-1 --> k
        # 2,k-2 --> k
        # 3,k-3 --> k
        d = {}
        for i in range(len(arr)):
            d[arr[i] % k] = d.get(arr[i] % k, 0) + 1
        
        # num1 = a1 + (k * b1), a1,b1 are integers, and 0 <= a1 < k
        # num2 = a2 + (k * b2), a2,b2 are integers, and 0 <= a2 < k

        # num1 + num2                        is divisible by k
        # <--> a1 + (k * b1) + a2 + (k * b2) is divisible by k
        # <--> a1 + a2 + k(b1) + k(b2)       is divisible by k
        # <--> a1 + a2 + k(b1 + b2)          is divisible by k
        # <--> a1 + a2                       is divisible by k

        
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
        for key in d:
            if d[key] != d.get(k - key, 0):
                return False
        
        return True