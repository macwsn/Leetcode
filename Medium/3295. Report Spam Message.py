class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        x = set(bannedWords)
        cnt = 0
        for mess in message:
            if mess in x: cnt += 1
        return cnt > 1