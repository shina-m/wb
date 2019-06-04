class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for n in nums:
            result += [ x + [n] for x in result]    
            
        return result
        