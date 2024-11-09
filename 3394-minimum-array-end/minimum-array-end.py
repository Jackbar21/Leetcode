class Solution:
    def minEnd(self, n: int, x: int) -> int:
        bin_x = bin(x)[2:]
        bin_num = bin(n - 1)[2:]

        # Add padding as needed
        if len(bin_num) > len(bin_x):
            bin_x = '0' * (len(bin_num) - len(bin_x)) + bin_x
        
        # 01101100000001
        # 01101100001001

        x_index = len(bin_x) - 1
        num_index = len(bin_num) - 1
        arr = collections.deque()
        while num_index >= 0:
            if x_index < 0:
                arr.appendleft(bin_num[num_index])
                num_index -= 1
                continue

            if bin_x[x_index] == '0':
                arr.appendleft(bin_num[num_index])
                num_index -= 1
                # x_index -= 1
            else:
                assert bin_x[x_index] == '1'
                arr.appendleft('1')
                # x_index -= 1

            # Loop Invariant
            x_index -= 1
            # assert x_index >= 0
            # num_index -= 1

        print(arr)

        return x | int(''.join(arr), 2)
        # base = 1
        # # nums = [x]
        # prev_num = x
        # new_biggest = x
        # count = 1



        while count < n:
            # prev_num = nums[-1]
            # new_nums = []
            for num in nums:
                new_num = num | base
                if new_num > prev_num:
                    assert new_num > new_biggest
                    # new_nums.append(new_num)
                    new_biggest = new_num
                    count += 1
            # if new_num > prev_num:
            #     nums.append(new_num)
            #     continue
            
            # Loop Invariant
            nums.extend(new_nums)
            base <<= 1
            prev_num = new_biggest
        
        # print(nums)
        return nums[n - 1]
