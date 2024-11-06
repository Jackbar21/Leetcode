class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        d = {} # num to #set-bits mappings
        for num in nums:
            d[num] = bin(num).count('1')

        INDEX, NUM = 0, 1
        index_dict = {} # index to desired index mappings
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[NUM])
        for desired_index in range(len(sorted_nums)):
            at_index = sorted_nums[desired_index][INDEX]
            index_dict[at_index] = desired_index
        
        for at_index in index_dict:
            desired_index = index_dict[at_index]
            set_bits = d[nums[at_index]]

            direction = 1 if at_index < desired_index else -1
            while at_index != desired_index:
                # next_index = (at_index + 1) if at_index < desired_index else (at_index - 1)
                next_index = at_index + direction
                next_num_set_bits = d[nums[next_index]]
                if set_bits != next_num_set_bits:
                    return False
                
                # Loop Invariant
                at_index = next_index

            # Case 1:
            # while at_index < desired_index:
            #     next_index = at_index + 1
            #     next_num = nums[next_index]
            #     next_num_set_bits = d[next_num]
            #     if set_bits != next_num_set_bits:
            #         return False
                
            #     # Loop Invariant
            #     # at_index += 1
            #     at_index = next_index
            
            # Redundant if statement
            # if at_index == desired_index:
            #     continue
            
            # Case 2:
            # while at_index > desired_index:
            #     next_index = at_index - 1
            #     next_num = nums[next_index]
            #     next_num_set_bits = d[next_num]
            #     if set_bits != next_num_set_bits:
            #         return False

        #print(sorted_nums)
        #print(index_dict)
        return True