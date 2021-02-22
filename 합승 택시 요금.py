from heapq import heappush, heappop
MAX_SIZE = 10000000


def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1
    adj = [[] for _ in range(n)]
    h = []
    for u, v, w in fares:
        u, v = u-1, v-1
        adj[u].append((v, w))
        adj[v].append((u, w))
    l = []
    for node in range(n):
        dist = [MAX_SIZE for _ in range(n)]
        dist[node] = 0
        heappush(h, (0, node))
        while h:
            _, curr = heappop(h)
            for nxt, cost in adj[curr]:
                if dist[curr] + cost < dist[nxt]:
                    dist[nxt] = dist[curr] + cost
                    heappush(h, (cost, nxt))
            if dist[a] + dist[b] + dist[s]:
                l.append(dist[a] + dist[b] + dist[s])

    return min(l)
