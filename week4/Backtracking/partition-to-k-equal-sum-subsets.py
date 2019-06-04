class Solution:
    
    def helper(self, num_index, target, sub_used):
        
        target = target - self.nums[num_index]
        
        if target < 0:
            self.memo[target] = False
            return 
           
        sub_used.add(num_index)
        
        if target in self.memo:
            return self.memo[target]
        
        elif target == 0:
            self.memo[target] = True
            return
        
        else:
            self.memo[target] = False
            for n_index in range(num_index+1, self.lc):
                if n_index not in self.index_used:
                    if self.helper(n_index, target, sub_used.copy()) == True:
                        self.memo[target] = True
                        sub_used.add(target)
                        self.index_used.update(sub_used)
                        break

        return self.memo[target]
                
                
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if k == 1:
            return True
        
        target = sum(nums) / k
        
        self.result = False
        
        if target % 1 != 0:
            return self.result
        
        #self.nums = sorted(nums)
        self.nums = nums
        self.lc = len(nums)
        self.index_used = set()
        
        for _ in range(k-1):
            self.memo = {}
            result = False
            for i in range(self.lc):                
                if self.helper(i, int(target), self.index_used):
                    result = True
                    break
                    
            if result == False: return False
                
        return True
    
        
        