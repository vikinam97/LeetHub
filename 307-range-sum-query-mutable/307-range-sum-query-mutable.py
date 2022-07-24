class NumArray:
    
    def generateTree(self, nums, l, r, idx):
        if l == r:
            self.segmentTree[idx] = nums[l]
            return nums[l]
        
        mid = l + ((r - l) // 2)
        
        lv = self.generateTree(nums, l, mid, 2 * idx)
        rv = self.generateTree(nums, mid+1, r, (2 * idx) + 1)
        
        self.segmentTree[idx] = lv + rv
        
        return self.segmentTree[idx]

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segmentTree = [0] * (4 * len(nums))
        self.generateTree(nums, 0, len(nums)-1, 1)

    def updateRecur(self, idx, l, r, pos, val):
        # print(l, r)
        if pos > r or pos < l:
            return self.segmentTree[idx]
        if l == r:
            # print(l, r, idx, self.segmentTree[idx])
            self.segmentTree[idx] = val
            # print(idx, self.segmentTree[idx])
            return self.segmentTree[idx]
        
        mid = l + ((r - l ) // 2)
        lv = self.updateRecur(2 * idx, l, mid, pos, val)
        rv = self.updateRecur((2 * idx) + 1, mid + 1, r, pos, val)
        
        self.segmentTree[idx] = lv + rv
        return self.segmentTree[idx]
        
    def update(self, index: int, val: int) -> None:
        self.updateRecur(1, 0, len(self.nums)-1, index, val)
        # print(self.segmentTree)

    def query(self, idx, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if l >= ql and r <= qr:
            return self.segmentTree[idx]
        
        mid = l + ((r - l ) // 2)
        lv = self.query(2 * idx, l, mid, ql, qr)
        rv = self.query((2 * idx) + 1, mid + 1, r, ql, qr)
        
        return lv + rv
    
    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, 0, len(self.nums)-1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)