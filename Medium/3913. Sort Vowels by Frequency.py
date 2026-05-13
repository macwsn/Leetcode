class Solution:
    def sortVowels(self, s: str) -> str:
        v = ['a','e','i','o','u']
        T = []
        d = dict()
        for vow in v: d[vow] = 0
        for i in range(len(s)):
            if s[i] in d: d[s[i]] += 1
            else: T.append(i) 
        L = sorted(zip(list(d.keys()), list(d.values())), key = lambda x: (-x[1], s.find(x[0])))
        cnt = 0
        x = ''
        for a,b in L: x += a * b
        y = ''
        for key in s:
            if key in v:
                y += x[cnt]
                cnt += 1
            else: y += key
        return y