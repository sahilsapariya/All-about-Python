n = 4
w = [1, 3, 4, 5]
p = [10, 40, 30, 70]
c = 7
t = [[0 for x in range(c+1)] for x in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, c+1):
        if j < w[i-1]:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = max(t[i-1][j], (p[i-1] + t[i-1][j - w[i-1]]))

for i in range(n+1):
    for j in range(c+1):
        print(t[i][j], end='\t')
    print()