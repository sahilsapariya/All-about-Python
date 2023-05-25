"""
    a = "abcde"
    b = "ace"

    so longest common sequence is "ace".
    In this problem we will return the  length of lcs.
"""

def longest_common_sequence(s1: str, s2: str) -> int:
    l1, l2 = len(s1), len(s2)

    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = 1 + dp[i][j]
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]

if __name__ == '__main__':
    s1 = "longest"
    s2 = "stone"

    ans = longest_common_sequence(s1, s2)

    print(ans)  # 3