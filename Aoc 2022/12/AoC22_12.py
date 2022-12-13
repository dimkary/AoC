# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:09:52 2022

@author: DKARYPID
"""
import networkx as nx
# from collections import defaultdict

### Part 1 ###
with open("./input.txt") as f:
    a = f.readlines()
    
grid = []
line_count = 0
G = nx.DiGraph()
ones = []
for line in a:
    col_count = 0
    row = []
    for char in line.strip():
        # print(line_count, col_count)        
      
        if char == 'S':
            row.append(1)
            start = (line_count, col_count)
            
        elif char == 'E':
            row.append(ord('z')-96)
            end = (line_count, col_count)
        else:
            if char == 'a':
                ones.append((line_count,col_count))
            row.append(ord(char)-96)
        G.add_node((line_count,col_count))
        col_count += 1  
    grid.append(row.copy())
    line_count += 1

length = len(grid[0])
height = len(grid)

for xy in G:
    # if xy[0] == 20:
    #     print(xy)
    left = (xy[0] - 1, xy[1])
    right = (xy[0] + 1, xy[1])
    up = (xy[0], xy[1] - 1)
    down = (xy[0], xy[1] + 1)
    
    neighbors = [left, right, up, down]
    for i in neighbors:
        if i[0] < 0 or i[0] > height - 1 or i[1] < 0 or i[1] > length - 1:
            continue
        else:
            if i:
                # print(xy, i)
                # print(grid[xy[0]][xy[1]], grid[i[0]][i[1]])
                # print(grid[xy[0]][xy[1]] - grid[i[0]][i[1]])
                pass
            if not (grid[xy[0]][xy[1]] - grid[i[0]][i[1]] <= -2):
                G.add_edge(xy, i)
                
print(len(nx.dijkstra_path(G, start, end))-1)
# nodes = nx.dijkstra_path(G, start, end)
# newG = nx.DiGraph()
# print(nx.dijkstra_path(G, start, end))
# pos = {(x,y):(y,-x) for x,y in G.nodes()}
# nx.draw(G,pos = pos ,with_labels = True, node_size=[grid[i[0]][i[1]] * 20 for i in G])



# for i in range(len(nodes)-1):
    # newG.add_edge(nodes[i], nodes[i+1])
# pos = {(x,y):(y,-x) for x,y in newG.nodes()}
# nx.draw(newG,pos = pos ,with_labels = True, node_size=[grid[i[0]][i[1]] * 20 for i in newG])    
totals = []
for i in ones:
    try:
        totals.append(len(nx.dijkstra_path(G, i, end))-1)
    except:
        pass
    
print(min(totals))