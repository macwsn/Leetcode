class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        val = 1
        res = ''
        if not s: return 0
        if s[0] == '-':
            val = -1
            s = s[1:]
        elif s[0] == '+': s = s[1:]
        cnt = 0
        while cnt < len(s) and s[cnt] == '0': cnt += 1
        s = s[cnt:]
        if not s: return 0
        cnt = 0
        while cnt < len(s) and 47 < ord(s[cnt]) < 58: cnt += 1
        res = s[:cnt]
        ret = int(res)*val if res else 0
        a = 2**31
        if ret < -a: return -a
        if ret > a - 1: return a - 1
        return ret


