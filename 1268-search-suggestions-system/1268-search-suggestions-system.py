class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)
        i, j = 0, n-1
        
        result = []
        print(products)
        for count, char in enumerate(searchWord):
            
            while i < n and (count >= len(products[i]) or char != products[i][count]):
                i += 1

            while j > 0 and (count >= len(products[j]) or char != products[j][count]):
                j -= 1
            
            if i > j:
                result.append([])
                continue
            
            result.append(products[i:min(j+1, i+3)])
        
        return result
        
            
            