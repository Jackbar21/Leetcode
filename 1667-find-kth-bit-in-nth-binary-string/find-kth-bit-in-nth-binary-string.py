class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # sol =

        # Size_0 = 1
        # Size_i = Size_(i-1) + 1 + Size(i - 1) = 2 * Size(i - 1) + 1
        arr = [0]

        for _ in range(n - 2 + 1):
            rest = list(map(lambda bit: 1 - bit, arr))[::-1]
            arr.append(1)
            arr.extend(rest)
        
        return str(arr[k - 1])
        
        print(arr)
        print(len(arr))
        print(len("011100110110001"))
        return "0"