class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        l = [x[::-1] for x in l]
        return ' '.join(l)