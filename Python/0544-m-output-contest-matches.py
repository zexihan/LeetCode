class Solution:
    def findContestMatch(self, n: int) -> str:
        team = [str(i) for i in range(1, n + 1)]

        while n > 1:
            for i in range(n // 2):
                team[i] = "({},{})".format(team[i], team.pop())
            n //= 2

        return team[0]
