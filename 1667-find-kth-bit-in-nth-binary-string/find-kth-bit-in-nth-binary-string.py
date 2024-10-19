class Solution:
    # Returns 0 or 1, as int.
    def findKthBitHelper(self, k, max_val):
        mid = max_val // 2

        if max_val <= 1:
            print(f"{max_val=}, {k=}")
            assert max_val == 1
            return 0
            

        if k <= mid:
            return self.findKthBitHelper(k, mid)
        
        if k == mid + 1:
            print(k, max_val, mid)
            return 1
        
        new_k = max_val - k + 1
        # assert new_k % 2 == 0
        return 1 - self.findKthBitHelper(new_k, mid)
        
        # assert k > mid + 1
        # mid + 1 -> max_val
        # mid + 2 -> max_val - 1
        # mid + 3 -> max_val - 2
        # ...
        # mid + i -> max_val - (i - 1) == max_val - i + 1
        # mid + i == max_val - i + 1
        # 2i == max_val - mid + 1
        # i == (max_val - mid + 1) 




    def findKthBit(self, n: int, k: int) -> str:
        arr = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]
        max_val = pow(2, n) - 1
        return str(self.findKthBitHelper(k, max_val))
    #     invert = False

    #     # k -= 1

    #     if k <= 1:
    #         return "0"

    #     i = 0
    #     while k < arr[i]:
    #         i += 1
        
    #     mid = (arr[i]-1) // 2
    #     if k == mid + 1:
    #         return "1"
        
    #     if k < mid:
    #         # 
        
    #     if k > mid:
    #         arr[i] - (k + 1)


    #     # arr = [0] # Starting with S_1
    #     # while k > len(arr):
    #     #     arr.append(1)
    #     #     arr.extend(1 - arr[i] for i in range(len(arr) - 2, -1, -1))
        
    #     # print(arr)
    #     # print(len(arr))
    #     # print(arr[31 - (k + 1)], arr[15 + ])
    #     # return str(arr[k - 1])

    
    # # [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575]

    # # Si = Si - 1 + "1" + reverse(invert(Si - 1))

    # # k'th index = len(Si) - X index of reverse(invert(Si - 1))
    # #   = len(Si) - (len(Si) - X) index of invert(Si - 1)
    # #   = X index of invert(Si - 1)



    # # 7