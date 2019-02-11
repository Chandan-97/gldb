# Ref : https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

# Dynamic Programming implementation of LCS problem

def lcs(X , Y):
	# find the length of the strings
	m = len(X)
	n = len(Y)

	# declaring the array for storing the dp values
	L = [[None]*(n+1) for i in range(m+1)]

	"""Following steps build L[m+1][n+1] in bottom up fashion 
	Note: L[i][j] contains length of LCS of X[0..i-1] 
	and Y[0..j-1]"""
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j] , L[i][j-1])

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
	return L[m][n]
#end of function lcs


# Driver program to test the above function
# X = "AGGTAB"
# Y = "GXTXAYB"
# print "Length of LCS is ", lcs(X, Y)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
# PS : Ref given for the code


t = int(input())
for _ in range(t):
    a = input()
    b = input()

    if lcs(a, b) < len(b):
        print("No")
        continue

    idx = [[] for i in range(len(b))]
    for i in range(len(b)):
        c = b[i]
        for j in range(len(a)):
            if(b[i] == a[j]):
                idx[i].append(j)

    print("Yes")
    if(len(b) == 1):
        print("0")
        continue

    if(len(b) == 2):
        ans = 100000000
        for i in idx[0]:
            for j in idx[1]:
                if(j > i):
                    ans = min(ans, j - i + 1 - len(b))
                    break
        print(ans)

    if(len(b) > 2):
        ans = 100000000
        xx = 20
        for st in idx[0]:
            if(xx < 0):
                break
            xx -= 1
            i = st
            j = 0
            match = 0
            while(i < len(a) and j < len(b)):
                if(a[i] == b[j]):
                    if match == len(b)-1: ans = min(ans, i - st + 1 - len(b)); break
                    i += 1; j += 1; match += 1
                else:
                    i += 1
        print(ans)