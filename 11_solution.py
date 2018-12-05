#!/usr/bin/env python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

largest_prod = 0

for i in range(0,20):
    for j in range (0,16):
        product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
        if product > largest_prod:
            largest_prod = product
        product = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
        if product > largest_prod:
            largest_prod = product
        
for i in range(0,16):
    for j in range (0,16):
        product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2]* grid[i+3][j+3]
        if product > largest_prod:
            largest_prod = product
            
for i in range(3,20):
    for j in range (0,16):
        product = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
        if product > largest_prod:
            largest_prod = product

print(largest_prod)
