# Python 3.5

def main():
    problem = open("C-large-practice.in", "r")
    output = open("C-out.txt", "w")

    T = int(problem.readline().strip())

    for test in range(T):
        line = problem.readline().strip().split()
        N = int(line[0])
        Q = int(line[1])
        horse = []
        for i in range(N):
            line = problem.readline().strip().split()
            horse.append([int(a) for a in line])
        graph = {}
        for i in range(N):
            line = problem.readline().strip().split()
            graph[i] = {}
            for j in range(N):
                if line[j] != "-1":
                    graph[i][j] = int(line[j])

        distance = {}
        for i in range(N):
            distance[i] = {}
            distance[i][i] = 0
            vertex = {}
            vertex[i] = 0
            for j in range(N):
                if i != j:
                    distance[i][j] = float("inf")
                    vertex[j] = float("inf")
            while vertex != {}:
                now_v = min(vertex, key=vertex.get)
                vertex.pop(now_v)
                for v in graph[now_v].keys():
                    new_dist = distance[i][now_v] + graph[now_v][v]
                    if new_dist < distance[i][v]:
                        distance[i][v] = new_dist
                        vertex[v] = new_dist
        for i in range(N):
            for j in range(N):
                if distance[i][j] == 0 or distance[i][j] == float("inf") or distance[i][j] > horse[i][0]:
                    distance[i][j] = float("inf")
                else:
                    distance[i][j] = distance[i][j] / horse[i][1]
        output.write("Case #" + str(test+1) + ": ")
        for i in range(Q):
            line = problem.readline().strip().split()
            start = int(line[0])-1
            end = int(line[1])-1
            dist = {}
            dist[start] = 0
            vertex = {}
            vertex[start] = 0
            for j in range(N):
                if j != start:
                    dist[j] = float("inf")
                    vertex[j] = float("inf")
            while vertex != {}:
                now_v = min(vertex, key=vertex.get)
                vertex.pop(now_v)
                for v in distance[now_v].keys():
                    new_dist = dist[now_v] + distance[now_v][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        vertex[v] = new_dist
            output.write(str(round(dist[end], 6)) + " ")
        output.write("\n")
    problem.close()
    output.close()

main()
