from queue import PriorityQueue

def find_shortest(G):
    n = len(G)
    pq = PriorityQueue()
    pq.put((G[0][0], 0, 0))
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    while not pq.empty():
        v_dist, v_x, v_y = pq.get()
        if v_x == n-1 and v_y == n-1:
            return v_dist
        
        for i in range(-1,2):
            for j in range(-1,2):
                if (j != 0 or i != 0) and 0 <= v_x+i < n and 0 <= v_y+j<n and visited[v_x+i][v_y+j] == False:
                    pq.put((v_dist + G[v_x+i][v_y+j], v_x+i, v_y+j))
                    visited[v_x+i][v_y+j] = True
        


if __name__ == "__main__":
    G = [[1, 1, 1, 9, 9, 9, 9, 9],
         [9, 9, 1, 9, 9, 9, 9, 9],
         [9, 9, 1, 9, 9, 1, 1, 1],
         [9, 9, 1, 9, 9, 1, 9, 1],
         [9, 1, 1, 1, 1, 1, 9, 1],
         [9, 9, 9, 9, 9, 9, 9, 1],
         [9, 9, 9, 9, 9, 9, 9, 1],
         [0, 0, 0, 0, 0, 0, 0, 1]]
    print(find_shortest(G))
