INF = 10 ** 20
v_num, e_num, root = map(int, input().split())
cost_list = [[] for i in range(v_num)]
dist = [INF for i in range(v_num)]

for i in range(e_num):
    source, target, cost = map(int, input().split())
    cost_list[source].append((target, cost))

u = list(range(v_num))
dist[root] = 0


while u:
    m = INF
    for i in u:
        if m > dist[i]:
            m = dist[i]
    w = u.index(m)
    print(m)
    print(u)
    print(w)
    print(dist)
    u.remove(w)
    for to, cost in cost_list[w]:
        c = dist[w] + cost
        if c < dist[to]:
            dist[to] = c

for i in dist:
    if i == INF:
        print("INF")
    else:
        print(i)
