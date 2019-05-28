    def sub_rob(self, start, end):
        
        if end == start:
            return self.n[end]
        
        else:
            self.memo[start][end-1] = self.memo[start][end-1] if self.memo[start][end-1] != None else self.sub_rob(start, end-1)
            
            if end-2 >= start:
                self.memo[start][end-2] = self.memo[start][end-2] if self.memo[start][end-2] != None else self.sub_rob(start, end-2)
                return max(self.n[end] + self.memo[start][end-2], self.memo[start][end-1])
            
            else:
                return max(self.n[end], self.memo[start][end-1])
        
        
        
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        
        self.n = nums
        self.memo = {0: [None] * l, 1: [None] * l}
        
        return max( self.sub_rob(1, l-1), self.sub_rob(0, l-2) )