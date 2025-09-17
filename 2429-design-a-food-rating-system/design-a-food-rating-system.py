class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_rating = {} # food: rating
        self.food_to_cuisine = {} # food: cuisine
        self.cuisine_max_heaps = defaultdict(list) # cuisine: max heap

        # assert len(foods) == len(cuisines) == len(ratings)
        N = len(foods)
        for i in range(N):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            heapq.heappush(self.cuisine_max_heaps[cuisine], (-rating, food))
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        max_heap = self.cuisine_max_heaps[cuisine]
        heapq.heappush(max_heap, (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        max_heap = self.cuisine_max_heaps[cuisine]
        while True:
            # assert len(max_heap) > 0
            rating, food = heapq.heappop(max_heap)
            # assert rating <= 0
            rating = -rating
            # assert rating >= 0

            if rating != (actual_rating := self.food_to_rating[food]):
                continue
            
            # assert rating == actual_rating
            heapq.heappush(max_heap, (-rating, food))
            return food



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)