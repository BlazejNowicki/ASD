def matrix_chain_order(p):
    n = len(p)-1
    m = [[0]*n for _ in range(n)]
    s = [[0]*n for _ in range(n)]
    for l in range(2,n+1):
        for i in range(0, n-l+1):
            j = i+l-1
            m[i][j] = None
            for k in range(i, j):
                q = m[i][k]+m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if m[i][j] is None or q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m[0][n-1], s

def print_optimal_parens(s,i,j):
    if i==j:
        print(i,end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")",end='')


if __name__ == "__main__":
    #(30,35)  (35,15)  (15,5)  (5,10)  (10,20)  (20,25)
    p = [30,35,15,5,10,20,25]
    min_cost, s = matrix_chain_order(p)
    print(min_cost)
    print_optimal_parens(s, 0, len(p)-2)
    print()