class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))   

        result = []
        for i in range(len(people)):
            h, k = people[i]
            # result.insert(k, people[i])
            result = result[:k] + [people[i]] + result[k:]
        
        return result
        
            