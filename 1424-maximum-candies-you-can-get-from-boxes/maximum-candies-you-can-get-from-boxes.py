class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        OPEN, CLOSED = 1, 0

        queue = collections.deque((box, False) for box in initialBoxes) # (box_index, seen_twice)
        # visited = set(initialBoxes)
        visited = set()
        max_candy = 0

        while queue:
            box_index, seen_twice = queue.popleft()

            # print(f"{box_index=}, {max_candy=}")
            if box_index in visited:
                continue

            if status[box_index] == CLOSED:
                if seen_twice:
                    # all elements in queue are unopened
                    # assert all(status[box] == CLOSED for box in queue)
                    # assert status[box_index] == CLOSED
                    break
                else:
                    queue.append((box_index, True))
                    continue
    
            visited.add(box_index)
            candy = candies[box_index]
            max_candy += candy

            for key in keys[box_index]:
                # print(f"{key=}")
                status[key] = OPEN
            
            for box in containedBoxes[box_index]:
                # print(f"containedBox={box}")
                if status[box] == OPEN:
                    queue.appendleft((box, False))
                else:
                    queue.append((box, False))
            
            # print(f"{queue=}")
            # print()

        return max_candy