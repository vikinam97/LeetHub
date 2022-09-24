class NumArray:

    
    def __init__(self, nums: List[int]):
        
        self.tree = [0]*(4*len(nums))
        self.nums = nums
        
        def generateTree(s, e, idx, nums):
            if s == e:
                self.tree[idx] = nums[s]
                return nums[s]
            mid = s + ((e - s) // 2)
            l = generateTree(s, mid, 2 *idx, nums)
            r = generateTree(mid+1, e, 2*idx+1, nums)

            self.tree[idx] = l + r
            return self.tree[idx]
        
        generateTree(0, len(nums)-1, 1, nums)
        
    def update(self, i: int, v: int) -> None:
        
        def recur(idx, s, e, index, val):
            if index < s or index > e:
                return self.tree[idx]
            if s == e:
                self.tree[idx] = val
                return val
            
            mid = s + ((e - s) // 2)
            l = recur(2*idx, s, mid, index, val)
            r = recur(2*idx+1, mid+1, e, index, val)
            
            self.tree[idx] = l + r
            return l + r
            
        recur(1, 0, len(self.nums)-1, i, v)
        

    def sumRange(self, left: int, right: int) -> int:
        
        def query(idx, s, e, qs, qe):
            if s > qe or e < qs:
                return 0
            if qs <= s and qe >= e:
                return self.tree[idx]
            
            mid = s + ((e - s) // 2)
            l = query(2*idx, s, mid, qs, qe)
            r = query(2*idx + 1, mid+1, e, qs, qe)
            
            return l+r
                        
        return query(1, 0, len(self.nums)-1, left, right)
    
    
        