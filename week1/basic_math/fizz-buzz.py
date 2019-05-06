class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        num = []
        for i in range(1, n+1):
            t = ''
            if i>=3 and i%3 == 0:
                t += 'Fizz'
            if i>=5 and i%5 == 0:
                t += 'Buzz'
            
            if t == '':
                t +=str(i)
                
            num.append(t)
        
        return num