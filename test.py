near_dups = {
"A": ["B", "I", "K"],
"B": ["A", "D"],
"C": ["E"],
"D": [],
"E": [],
"F": [],
"G": ["K"],
"I": [],
"K": [],
}


def findNearDups(adj):
  # union find style solution 

  nodes = set(adj.keys()) # O(n) adds every neighbor and key
  for val in adj.values():
    nodes.update(val)

  parent = {n: n for n in nodes} # initially every parent of each node is gonna be itself
  rank = {n: 0 for n in nodes} # initially going to be 0 and represents heught of tree

  def find(a): # find the parents of this node
    if parent[a] != a:
      parent[a] = find(parent[a])
    return parent[a]
  
  def union(a, b): 
    aParent = find(a)
    bParent = find(b)
    if aParent == bParent:
      return False
    else:
      if rank[aParent] < rank[bParent]:
        parent[aParent] = bParent
      elif rank[bParent] < rank[aParent]:
        parent[bParent] = aParent
      else:
        parent[bParent] = aParent
        rank[aParent] += 1
  for i in adj:
    for j in adj[i]:
      union(i, j)
  numDuplicates = set(parent.keys())
  return len(numDuplicates)

from collectons import deque
def find_path(maze, si, sj, ei, ej, N):

  q = deque([(si, sj, N, 0)])
  visited = set()
  visited.add((si, sj, N))
  while q:
    i, j, lives, steps = q.popleft()
    if i == ei and j == ej:
      return steps
    for dr, dc in [(0, -1), (1, 0), (-1, 0), (0, 1)]:
      newI = i + dr
      newJ = j + dc
      if newI < 0 or newJ < 0 or newI >= len(maze) or newJ >= len(maze[0]):
        continue

      if maze[newI][newJ] == 1:
        continue
      if maze[newI][newJ] == 6:
        if (newI, newJ, lives - 1) in visited: # not sure if this is the correct state or need to include lives
          continue
        if lives > 0:
          visited.add((newI, newJ, lives))
          q.append((newI, newJ, lives - 1, steps + 1))
      else:
        if (newI, newJ, lives) in visited: # not sure if this is the correct state or need to include lives
          continue
        visited.add((newI, newJ, lives))
        q.append((newI, newJ, lives, steps + 1))
  return -1
  