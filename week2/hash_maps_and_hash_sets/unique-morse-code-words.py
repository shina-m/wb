class Solution:
    def convert_to_morse(self, w):
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        base = ord('a')
        
        w_code = []
        for s in w:
            index = ord(s)-base
            w_code.append(code[index])
        
        return ''.join(w_code)
        
        
        
        
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = []
        
        for w in words:
            result.append(self.convert_to_morse(w))
            
        return len(set(result))