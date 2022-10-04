import collections


# Binary search

# Iterative method
def binary_iterative(arr, x, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Recursive method
def binary_recursive(arr, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_recursive(arr, x, low, mid - 1)
        else:
            return binary_recursive(arr, x, mid + 1, high)
    else:
        return -1


# Breadth-first search (BFS)
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Depth-first search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)

    return visited


# Linear search
def linear(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
