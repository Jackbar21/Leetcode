class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # assert len(position) == len(speed)
        POSITION, SPEED = 0, 1
        n = len(position)

        pos_speed = [(position[i], speed[i]) for i in range(n)]
        pos_speed.sort(key = lambda pair: pair[POSITION], reverse=True)

        # Skip first car, since it's part of first fleet
        first_car_pos, first_car_speed = pos_speed[0]
        handicap = (target - first_car_pos) / first_car_speed
        num_fleets = 1

        for i in range(1, len(pos_speed)):
            # If current car can CATCH UP to previous car, it belongs in same fleet
            # Otherwise, it creates its own fleet, and at BEST all remaining cars
            # will join this new fleet or create their own (since they have smaller
            # starting positions, and passing a car is NOT allowed!)
            car_pos, car_speed = pos_speed[i]
            cur_moves = (target - car_pos) / car_speed
            if cur_moves > handicap:
                # Cannot catch up to car, so creates it's own fleet! And remember,
                # remaining cars, can only perform AT BEST the same as this car now!
                # Since again, surpassing cars is NOT allowed, and all remaining cars
                # start off at an earlier position (since speed_pos is sorted by 
                # non-increasing positions!).
                num_fleets += 1
                handicap = cur_moves

        return num_fleets
