class Solution:
    def helper(self, cand_index, temp_res, target):
        
        if target < self.candidates[cand_index]:
            return
        
        target = target - self.candidates[cand_index]
        temp_res.append(self.candidates[cand_index])
        
        if target == 0:
            self.result.append(temp_res)
        else:
            for c_index in range(cand_index, self.lc):
                t = target
                self.helper(c_index, temp_res.copy(), t)
            
        
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.candidates = candidates
        self.lc = len(candidates)
        
        for i in range(self.lc): 
            self.helper(i, [], target)
                
        return self.result
    
        