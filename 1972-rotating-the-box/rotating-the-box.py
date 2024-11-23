class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        return zip(*[
            self.applyHorizontalGravity(row)
            for row in box
        ][::-1])
    
    def applyHorizontalGravity(self, row):
        queue = collections.deque()

        STONE, OBSTACLE, EMPTY = '#', '*', '.'
        for i in range(len(row) - 1, -1, -1):
            item = row[i]
            assert item in [STONE, OBSTACLE, EMPTY]
            if item == EMPTY:
                queue.append(i)
                continue
            
            assert item in [STONE, OBSTACLE]
            if item == OBSTACLE:
                # queue.clear() # TODO: check if re-initialization is faster
                queue = collections.deque()
                continue
            
            assert item == STONE
            if len(queue) > 0:
                index = queue.popleft()
                assert row[index] == EMPTY
                row[index] = STONE
                assert row[i] == STONE
                row[i] = EMPTY
                queue.append(i)
        
        return row
