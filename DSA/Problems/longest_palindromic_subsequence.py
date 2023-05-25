"""
    Here we want to find the longest palindromic subsequence,
    we will be given a string then find the longest common subsequece 
    of given string with it's reverse order. This will give us results 
    of longest palindromic subsequence.
"""

def longest_common_sequence(s1: str, s2: str) -> int:
    l1, l2 = len(s1), len(s2)

    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1):
        for j in range(l2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1]


if __name__ == '__main__':
    s1 = "bbbab"
    s2 = s1[::-1]

    ans = longest_common_sequence(s1, s2)

    print(ans)  # 4