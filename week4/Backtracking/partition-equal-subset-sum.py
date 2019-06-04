class Solution:
    def helper(self, num_index, target):
        
        if target < self.nums[num_index]:
            self.memo[target] = False
            return 
         
        target = target - self.nums[num_index]
        
        if target in self.memo:
            return self.memo[target]
        
        elif target == 0:
            self.memo[target] = True
            return
        
        else:
            self.memo[target] = False
            for n_index in range(num_index+1, self.lc):
                t = target
                if self.helper(n_index, t) == True:
                    self.memo[target] = True
                    break
                    
        return self.memo[target]
                
                
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums) / 2
        
        if target % 1 != 0:
            return False
        
        
        self.nums = nums
        self.lc = len(nums)
        self.memo = {}
        
        for i in range(self.lc): 
            if self.helper(i, int(target)):
                return True
                
        return False
    
        