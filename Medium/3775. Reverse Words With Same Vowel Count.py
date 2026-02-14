class Solution:
    def reverseWords(self, s: str) -> str:
        v = ['a','e','i','o','u']
        c = 0
        words = s.split()
        for el in words[0]:
            if el in v: c += 1
        for i in range(1,len(words)):
            cnt = 0
            for el in words[i]: 
                if el in v: cnt += 1
            if cnt == c:
                words[i] = words[i][::-1]
        return " ".join(words)