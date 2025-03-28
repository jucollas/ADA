
k = 0
tree = []

def max_disjoint_paths(node, parent):
    height = 0
    ans = 0
    for child in tree[node]:
      if child != parent:
        paths_child, height_child = max_disjoint_paths(child, node, tree)
        ans += p
        height = max(height, h + 1)

    if height + 1 == k:
      ans += 1
      height = 0

    return ans, height

def max_disjoint_paths(n, k, edges):
    tree = [[] for _ in range(n)]

    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    max_paths = [0]
    dfs(0, -1, k, tree, max_paths)
    return max_paths[0]

if __name__ == "__main__":
    n, k = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

    print("Máximo número de caminos disjuntos de longitud", k, ":", max_disjoint_paths(n, k, edges))
