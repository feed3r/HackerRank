#!/bin/python3

import sys


def get_key_by_coord(m, i, j):
    return i * m + j


filepath = 'InputExample.txt'
fp = open(filepath)

n, m, k = fp.readline().strip().split(' ')
n, m, k = [int(n), int(m), int(k)]
coord_key = 0
maze = []
graph = {}
for a0 in range(n):
    row = fp.readline().strip()
    for cell_value in row:
        maze.append(cell_value)
        coord_key += 1

for a0 in range(k):
    i1, j1, i2, j2 = fp.readline().strip().split(' ')
    i1, j1, i2, j2 = [int(i1), int(j1), int(i2), int(j2)]

for i in range(n):
    for j in range(m):
        key = get_key_by_coord(m, i, j)
        graph[(i,j)] = []
        if maze[key] != '#': #element is not wall
            if j < m - 1 and maze[key + 1] != '#':
                graph[(i,j)].append((i, j + 1))  # add the RIGHT element
            if i < n - 1 and maze[key + m] != '#':
                graph[(i,j)].append((i + 1, j))  #add the LOWER element
            if j > 0  and maze[key - 1] != '#':
                graph[(i,j)].append((i, j - 1))  # add the LEFT element
            if i > 0 and maze[key - m] != '#':
                graph[(i,j)].append((i - 1, j))  #add the UPPER element

print(graph)