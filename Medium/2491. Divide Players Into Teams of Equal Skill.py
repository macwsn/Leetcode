class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        import collections
        n = len(skill)
        if n%2 != 0: return -1
        if n == 2: return skill[0]*skill[1]
        s = collections.Counter(skill)
        l = list(s.keys())
        l.sort()
        n = len(l)
        if n == 1:
            if s[l[0]]%2 == 1: return -1
            else: return s[l[0]] // 2 * (l[0])**2
        t = l[0] + l[-1]
        if s[l[0]] != s[l[-1]]: return -1
        suma = 0
        for i in range(1,len(l)//2):
            print(l[i],l[n-i-1])
            if  s[l[i]] != s[l[n-i-1]] or l[i] + l[n-i-1] != t : return -1
            else: suma+= l[i] * l[n-i-1] * s[l[i]]
        if n %2 != 0:
            if 2 * l[len(l)//2]!= t : return -1
            else: suma+= (l[len(l)//2]** 2) * s[l[len(l)//2]] //2
        return suma + l[0]*l[-1]*s[l[0]]        