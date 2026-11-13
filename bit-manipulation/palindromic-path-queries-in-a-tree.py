class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        s = list(s)
        bit = lambda c: 1 << (ord(c) - 97)

        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        base = [0] * n          # root->node parity mask for the ORIGINAL string

        # iterative DFS (no recursion limit issues)
        timer = 0
        base[0] = bit(s[0])
        stack = [(0, 0, 0)]     # (node, parent, state)
        up[0][0] = 0
        while stack:
            v, p, state = stack.pop()
            if state == 0:
                tin[v] = timer
                timer += 1
                stack.append((v, p, 1))
                for w in adj[v]:
                    if w != p:
                        up[0][w] = v
                        depth[w] = depth[v] + 1
                        base[w] = base[v] ^ bit(s[w])
                        stack.append((w, v, 0))
            else:
                tout[v] = timer - 1

        for k in range(1, LOG):
            prev, cur = up[k - 1], up[k]
            for v in range(n):
                cur[v] = prev[prev[v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff >> k & 1:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        # Fenwick tree with XOR: range update, point query
        tree = [0] * (n + 2)

        def add(i, m):
            i += 1
            while i <= n + 1:
                tree[i] ^= m
                i += i & -i

        def query(i):
            i += 1
            r = 0
            while i > 0:
                r ^= tree[i]
                i -= i & -i
            return r

        def P(v):
            return base[v] ^ query(tin[v])

        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                x, c = int(parts[1]), parts[2]
                delta = bit(s[x]) ^ bit(c)
                if delta:
                    add(tin[x], delta)
                    add(tout[x] + 1, delta)
                    s[x] = c
            else:
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                mask = P(u) ^ P(v) ^ bit(s[l])
                answer.append(mask & (mask - 1) == 0)
        return answer