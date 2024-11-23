class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row_index in range(len(box)):
            self.applyHorizontalGravity(box, row_index)

        return zip(*box[::-1])
        return zip(*[
            self.applyHorizontalGravity(row)
            for row in box
        ][::-1])
    
    def applyHorizontalGravity(self, box, row_index):
        queue = collections.deque()
        row = box[row_index]

        STONE, OBSTACLE, EMPTY = '#', '*', '.'
        for i in range(len(row) - 1, -1, -1):
            item = row[i]
            # assert item in [STONE, OBSTACLE, EMPTY]
            if item == EMPTY:
                queue.append(i)
                continue
            
            # assert item in [STONE, OBSTACLE]
            if item == OBSTACLE:
                queue.clear() # TODO: check if re-initialization is faster
                # queue = collections.deque()
                continue
            
            # assert item == STONE
            if len(queue) > 0:
                index = queue.popleft()
                # assert row[index] == EMPTY
                box[row_index][index] = STONE
                # assert row[i] == STONE
                box[row_index][i] = EMPTY
                queue.append(i)
        
        return row
