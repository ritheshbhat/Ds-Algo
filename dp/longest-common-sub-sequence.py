

def lcs(m,n,a,b,s):

    if m == 0 or n ==0:
        return s
    if a[m-1]==b[n-1]:
        s+=1
        return lcs(m-1,n-1,a,b,s)
    else:
        return max(lcs(m-1,n,a,b,s), lcs(m,n-1,a,b,s))


def lcs_with_dp(m,n,a,b,dp):
    if m ==0 or n == 0:
        return 0

    if dp[m-1][n-1]!=-1:
        return dp[m-1][n-1]

    if dp[m-1]==dp[n-1]:
        dp[m-1][n-1] = 1 +lcs_with_dp(m-2,n-2,a,b,dp)
        return dp[m-1][n-1]
    else:
        dp[m][n] = max(lcs_with_dp(m,n-2,a,b,dp), lcs_with_dp(m-2,n,a,b,dp))
        return dp[m][n]

def lcs_with_tabulation(a,b,dp):
    for i in range(1,len(a)):
        for j in range(1,len(b)):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    print(dp[len(a)-1][len(b)-1])


if __name__=="__main__":
    fs = "abcdab"
    ss = "acxdy"
    dp = [[ -1 for i in range(len(ss)) ]for j in range(len(fs))]
    # print(lcs(len(fs),len(ss),fs,ss,0))


    print(lcs_with_dp(len(fs),len(ss),fs,ss,dp))

    dp = [[ 0 for i in range(len(ss)) ]for j in range(len(fs))]


    lcs_with_tabulation(fs,ss,dp)