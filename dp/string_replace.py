'''
Created on Jul 14, 2018

@author: agautam1
'''

def naiveEditDistance(str1, str2, m, n):
    """
    Arguments:
        str1: String 1
        str2: String 2
        m: length of string 1
        n: length of string 2
    """
    if m == 0:
        return n
    if n == 0:
        return m
    
    if str1[m-1] == str2[n-1]:
        return naiveEditDistance(str1, str2, m-1, n-1)
    
    return 1 +  min(naiveEditDistance(str1, str2, m, n-1),       #insert
                    naiveEditDistance(str1, str2, m-1, n-1),     #replace
                    naiveEditDistance(str1, str2, m-1, n))       #remove



def editDistance(str1, str2, m, n):
    """
    Arguments:
        str1: String 1
        str2: String 2
        m: length of string 1
        n: length of string 2
    """
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],      #insert
                                   dp[i-1][j-1],    #replace
                                   dp[i-1][j])      #remove
    return dp[m][n]


if __name__ == '__main__':
    
    print editDistance('ABM', 'AMZ', 3, 3)
    
    
    
    