def solution(cards: list[int]) -> int:
    n = len(cards)
    dp = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = cards[i]
        for j in range(i+1, n):
            dp[i][j] = max(cards[i] + min(dp[i+2][j], dp[i+1][j-1]), cards[j] + min(dp[i+1][j-1], dp[i][j-2]))

    return dp[0][n-1]