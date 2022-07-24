from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hashSet = {}
        self.cuisineSet = defaultdict(lambda: SortedList())
        self.foodCuisineMap = {}
        for i in range(len(foods)):
            self.foodCuisineMap[foods[i]] = cuisines[i]
            self.hashSet[foods[i]] = (-1 * ratings[i], foods[i])
            self.cuisineSet[cuisines[i]].add(self.hashSet[foods[i]])
        
    def changeRating(self, food: str, newRating: int) -> None:
        prev = self.hashSet[food]
        self.hashSet[food] = (-1 * newRating, food)
        self.cuisineSet[self.foodCuisineMap[food]].remove(prev)
        self.cuisineSet[self.foodCuisineMap[food]].add(self.hashSet[food])
        return ""
        

    def highestRated(self, cuisine: str) -> str:
        # print([(foodnode.food, foodnode.rate) for foodnode in self.cuisineSet[cuisine]])
        return self.cuisineSet[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)