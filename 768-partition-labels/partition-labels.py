class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        N = len(s)
        leftmost_indices = {}
        rightmost_indices = {}

        for i, letter in enumerate(s):
            if letter not in leftmost_indices:
                leftmost_indices[letter] = i
            rightmost_indices[letter] = i
        
        print(f"{leftmost_indices=}")
        print(f"{rightmost_indices=}")

        groups = []
        cur_size = 0
        for letter, leftmost_index in leftmost_indices.items():
            rightmost_index = rightmost_indices[letter]
            if leftmost_index >= cur_size:
                groups.append(rightmost_index + 1 - cur_size)
                cur_size = rightmost_index + 1
                continue
            
            assert leftmost_index < cur_size
            if rightmost_index >= cur_size:
                diff = rightmost_index + 1 - cur_size
                groups[-1] += diff
                cur_size = rightmost_index + 1

            
            # if rightmost_index <= cur_size:
            #     continue
            # else:

            
            # print(f"{leftmost_index=}, {cur_size=}, {rightmost_index=}")
            continue
            
            # Need to create a new group
            if leftmost_index >= cur_size:
                new_group_length = rightmost_index - leftmost_index + 1
                groups.append(new_group_length)
                continue
            
            groups[-1] = max(groups[-1], rightmost_index + 1 - sum(groups))
        
        return groups
            

