class Solution:
    def __init__(self):
        self.target = None
        self.pos_speed = None
        self.car_to_moves = {} # number of moves it takes for car to reach target
    
    def getNumMoves(self, car_index):
        # if car_index in self.car_to_moves:
        #     return self.car_to_moves[car_index]
        
        POSITION, SPEED = 0, 1
        car_pos = self.pos_speed[car_index][POSITION]
        car_speed = self.pos_speed[car_index][SPEED]

        # res = math.ceil((self.target - car_pos) / car_speed)
        res = (self.target - car_pos) / car_speed
        # self.car_to_moves[car_index] = res
        return res

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        assert len(position) == len(speed)
        n = len(position)
        POSITION, SPEED = 0, 1
        pos_speed = [(position[i], speed[i]) for i in range(n)]
        pos_speed.sort(key = lambda pair: pair[POSITION], reverse=True)
        self.pos_speed = pos_speed
        self.target = target

        # car_to_fleet = {}
        prev_car = None
        num_fleets = 1
        handicap = self.getNumMoves(0)
        # car_to_moves = {} 
        # car_to_moves[0] = math.ceil((target - pos_speed[0][POSITION]) / pos_speed[0][SPEED])
        for i, (pos, speed) in enumerate(pos_speed):
            # Skip first car, since it's part of first fleet
            if i == 0:
                continue

            # If current car can CATCH UP to previous car, it belongs in same fleet
            # Otherwise, it creates its own fleet, and at BEST all remaining cars
            # will join this new fleet or create their own (since they have smaller
            # starting positions, and passing a car is NOT allowed!)
            prev_car = i - 1
            prev_moves = self.getNumMoves(prev_car)

            cur_moves = self.getNumMoves(i)
            # if cur_moves <= prev_moves:
            if cur_moves <= handicap:
                # Joins same fleet, so nothing happens
                pass
            else:
                # Cannot catch up to car, so creates it's own fleet! And remember,
                # remaining cars, can only perform AT BEST the same as this car now!
                # Since again, surpassing cars is NOT allowed, and all remaining cars
                # start off at an earlier position (since speed_pos is sorted by 
                # non-increasing positions!).
                num_fleets += 1
                handicap = cur_moves

        




        return num_fleets


        
        
        