class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # return zip(*[
        #     self.applyHorizontalGravity(row)
        #     for row in box
        # ][::-1])
        res = [
            self.applyHorizontalGravity(row)
            for row in box
        ]
        # return zip(*res)

        for row in res:
            print(row)
            
        # Step 1: Transpose res
        m, n = len(res), len(res[0])
        new_res = [[-1] * m for _ in range(n)]
        for i in range(len(res)):
            for j in range(len(res[i])):
                # res[i][j], res[j][i] = res[j][i], res[i][j]
                new_res[j][i] = res[i][j]
            
        print("APPLY TRANSPOSE...")
        for row in new_res:
            print(row)

        # Step 2: Reverse rows of res
        # return res
        return [
            row[::-1]
            for row in new_res
        ]

    
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
                queue.clear() # TODO: check if re-initialization is faster
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
