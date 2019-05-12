class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.translate(str.maketrans("!?',;.", '      ')).replace('  ', ' ')
        p_count = collections.Counter( p.lower().split(' ') )
        
        for k,v in p_count.most_common():
            if k not in banned:
                return k
            
        