<h2>Nearest Neighbour Algorithm in Python</h2>

![Graph](https://i.imgur.com/Pt080Op.png)
```language
1. Pick a vertex randomly from graph and mark it as current vertex and add it to visited vertices list.
2. Find the shortest edge from current vertex to one of the connected and unvisited vertices.
3. Mark the next vertex as current vertex and add it to visited vertices list.
4. Repeat until all vertices visited or no possible path remained with unvisited vertices.
```

Since Nearest Neighbour Algorithm is a greedy algorithm, it may not find the shortest path or a complete path.
