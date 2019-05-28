class Solution:

# dp
    def sub_rob(self, nums: List[int]) -> int:
        stages =  len(nums)
        
        if stages == 1:
            return nums[0]
        
        memo = [0] * stages
        
        #Boundary Conditions
        memo[0] = max(nums[0], 0)
        memo[1] = max(nums[1], memo[0])
        
        
        for i in range(2, stages):           
            memo[i] = max(nums[i] + memo[i-2], memo[i-1])
                
        return memo[-1]
        
        
        
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        elif len(nums) == 1:
            return nums[0]
        
        return max( self.sub_rob(nums[1:]), self.sub_rob(nums[:-1]) ) 