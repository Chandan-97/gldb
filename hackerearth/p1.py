# Because You look Gorgeous in Black
# I don't know why I can't say this when we are alone

# Ref : https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
# Python program to print connected
# components in an undirected graph

from collections import deque

class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp += 1

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp

    # method to add an undirected edge
    def addEdge(self, v, w):
        v -= 1; w -= 1
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)

        for v in range(self.V):
            if visited[v] == False:
                temp = 0
                # cc.append(self.DFSUtil(temp, v, visited))
                q = deque()
                q.append(v)
                while(len(q) != 0):
                    node = q.popleft()
                    temp += 1
                    visited[node] = True
                    for child in self.adj[node]:
                        if visited[child] == False:
                            q.append(child)
                cc.append(temp)
        # print(cc)
        return cc

    # Driver Code


# if __name__ == "__main__":
#     # Create a graph given in the above diagram
#     # 5 vertices numbered from 0 to 4
#     g = Graph(5);
#     g.addEdge(1, 0)
#     g.addEdge(2, 3)
#     g.addEdge(3, 4)
#     cc = g.connectedComponents()
#     print(cc)

# This code is contributed by Abhishek Valsan
# PS : Ref Given on Top

n, k = map(int, input().split())
g = Graph(n)
for _ in range(n-1):
    u, v = map(int, input().split())
    if u > v : u,v = v, u
    if u < k: continue
    g.addEdge(u, v)
cc = g.connectedComponents()
ans = 0
for x in cc:
    ans += (x * (x-1)) // 2
print(ans)