def mirror_image_matrix(N, matrix):
    for row in matrix:
        print(" ".join(map(str,row[::-1])))
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int,input().split())))
mirror_image_matrix(N, matrix)
