class Solution:
    def __init__(self):
        self.obstacles = None
        self.dir_map = { 
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }

    def getDistance(self, origin, dest):
        x1, y1 = origin
        x2, y2 = dest
        return pow((x1 - x2), 2) + pow((y1 - y2), 2)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ORIGIN = (0, 0)
        x, y = ORIGIN # current position (initially origin point)
        cur_dir = "north" # i.e. "north", "east", "south", or "west"
        self.obstacles = set(tuple(obstacle) for obstacle in obstacles)
        max_dist = 0

        for command in commands:
            # Turn left
            if command == -2:
                cur_dir = self.changeDirection(cur_dir, "left")
                continue

            # Turn right
            if command == -1:
                cur_dir = self.changeDirection(cur_dir, "right")
                continue
            
            # Move k steps forward
            k = command
            assert 1 <= k <= 9
            # Idea: want to move up to k steps forward. We can do this
            # with a for loop that iterates up to k times, moving 1 step
            # for each for-loop iteration, and in each iteration checking
            # if stepping would cause us to hit an obstacle. If so then we
            # break, otherwise we update the current robot's position, as
            # well as updating the maximum squared Euclidian distance
            # found so far (if the current position happens to be the largest).
            for _ in range(k):
                assert cur_dir in self.dir_map
                dx, dy = self.dir_map[cur_dir]
                new_pos = (x + dx, y + dy)
                if self.isObstacle(new_pos):
                    break

                x, y = new_pos
                new_dist = self.getDistance(ORIGIN, new_pos)
                max_dist = max(max_dist, new_dist)     

        return max_dist
    
    def changeDirection(self, cur_dir, turn_direction):
        assert turn_direction in ["left", "right"]
        return self.turnLeft(cur_dir) if turn_direction == "left" else self.turnRight(cur_dir)
    
    def turnLeft(self, cur_dir):
        d = {
            "north": "west",
            "west": "south",
            "south": "east",
            "east": "north"
        }
        assert cur_dir in d
        return d[cur_dir]
    
    def turnRight(self, cur_dir):
        d = {
            "north": "east",
            "east": "south",
            "south": "west",
            "west": "north"
        }
        assert cur_dir in d
        return d[cur_dir]

    def isObstacle(self, pos):
        x, y = pos
        return (x, y) in self.obstacles