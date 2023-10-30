def lcs(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if arr2[i-1] == arr1[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]

print(lcs("AGGTAB", "GXTXAYB"))
