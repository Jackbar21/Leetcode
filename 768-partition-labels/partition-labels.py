class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        leftmost_indices = {}
        rightmost_indices = {}

        for i, letter in enumerate(s):
            if letter not in leftmost_indices:
                leftmost_indices[letter] = i
            rightmost_indices[letter] = i

        groups = []
        cur_size = 0
        for letter, leftmost_index in leftmost_indices.items():
            rightmost_index = rightmost_indices[letter] + 1
            if leftmost_index >= cur_size:
                groups.append(rightmost_index - cur_size)
                cur_size = rightmost_index
                continue
            
            # assert leftmost_index < cur_size
            # Since leftmost_index < cur_size, this letter must take part of a currently
            # existing group. Hence if its rightmost index is larger than (or equal to)
            # cur_size, then we must extend last group to include all of current letter's instances!
            if rightmost_index > cur_size:
                diff = rightmost_index - cur_size
                groups[-1] += diff
                cur_size += diff
        
        return groups
