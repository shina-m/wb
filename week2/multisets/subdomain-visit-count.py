class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        r = collections.Counter()
        
        for call in cpdomains:
            x = call.split(' ')
            count = int(x[0])
            
            d = x[1].split('.')
            
            for i in range(len(d)):
                r['.'.join(d[-i+1:])] += count
           
        return ['{0} {1}'.format(k,v) for v,k in r.items()]