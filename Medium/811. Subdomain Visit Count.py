class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for v in cpdomains:
            num, link = v.split(" ")
            links = link.split(".")
            for i in range(len(links)):
                s = ".".join(links[i:])
                if s not in d: d[s] = int(num)
                else: d[s] += int(num) 
        res = []
        l = list(d.keys())
        for x in l:
            res.append(str(d[x]) + " " + x)
        return res