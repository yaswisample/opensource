def transpose_matrix(matrix, N):
    transposed = [[matrix[j][i] for j in range(N)] for i in range(N)]
    return transposed
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
transposed_matrix = transpose_matrix(matrix, N)
for row in transposed_matrix:
    print(*row)
