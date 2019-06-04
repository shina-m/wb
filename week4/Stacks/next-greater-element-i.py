class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
            
        nums2_dict = {}
        for i,x in enumerate(nums2):
            nums2_dict[x] = i 
        
        res = []
        for i,x in enumerate(nums1):
            r = -1
            for j in range(nums_dict[x], len(nums2)):
                if nums2[j] >x:
                    r = nums2[j]
                    break
                    
            res.append(r) 
            
        return res