class Solution(object):
    def replaceWords(self, d, s):
        T = s.split()
        t = set(d)
        R = []
        for v in T:
            i = 1
            while i < len(v):
                a = v[:i]
                if a in t:
                    R.append(a)
                    i = len(v) + 2
                else: i += 1
            if i != len(v) + 2: R.append(v)
        return " ".join(R)   
        