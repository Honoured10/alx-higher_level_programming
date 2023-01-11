#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    tri = [[1]*(i+1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
    return tri
