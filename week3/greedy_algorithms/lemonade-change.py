class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = collections.Counter()
        for x in bills:
            if x == 10:
                if 5 in change and change[5] > 0:
                    change[5] -= 1
                else:
                    return False
            
            elif x == 20:
                y = x-5
                if 10 in change and change[10] > 0:
                    change[10] -= 1
                    y -= 10
                if 5 in change and change[5] >= y/5:
                    change[5] -= y/5
                else:
                    return False
                       
            change[x] += 1
                
     
        return True
        