def solution(cards: list[int]) -> int:
    n = len(cards)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = cards[i]
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
n            dp[i][j] = max(cards[i] + min(dp[i+2][j], dp[i+1][j-1]),
                          cards[j] + min(dp[i][j-2], dp[i+1][j-1]))
    return dp[0][n-1]