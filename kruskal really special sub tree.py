#!/bin/python3



if __name__ == '__main__':
    g_nodes, g_edges = map(int, input().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().split())
    visited = [0] * g_nodes
    for i in range(1, g_edges):
        value = g_weight[i]
        value1 = g_from[i]
        value2 = g_to[i]
        j = i - 1
        while (g_weight[j] > value and j >= 0):
            g_weight[j + 1] = g_weight[j]
            g_from[j + 1] = g_from[j]
            g_to[j + 1] = g_to[j]
            j = j - 1
        g_weight[j + 1] = value
        g_from[j + 1] = value1
        g_to[j + 1] = value2
    visited = [0] * (g_nodes)
    s = 0
    k = 0
    s = s + g_weight[0]
    visited[g_to[0] - 1] = g_from[0]
    visited[g_from[0] - 1] = g_from[0]
    k = k + 1
    for i in range(1, g_edges):
        if visited[g_to[i] - 1] == 0:
            visited[g_to[i] - 1] = g_from[i]
            s = s + g_weight[i]
            k = k + 1
            if k == (g_nodes - 1):
                break
        else:
            i = i + 1

    print(s)









    # Write your code here.
