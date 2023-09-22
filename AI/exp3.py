#program for BFS and DFS
graph = {
  'A' : ['B','C','D'],
  'B' : ['A','E', 'F'],
  'C' : ['A','F'],
  'D' : ['A'],
  'E' : ['B'],
  'F' : ['B','C']
}

closenode = []
opennode = []

#BFS
def bfs(closenode, graph, node, target, opennode):
  closenode.append(node)
  opennode.append(node)
  path = ""
  count = 0
  goal = 0

  while opennode:
    s = opennode.pop(0)

    if s not in graph:
      goal = 1
      print("Error: The start node is not in graph")
      break
    
    for neighbour in graph[s]:
      if neighbour not in closenode:
        closenode.append(neighbour)
        opennode.append(neighbour)
        if neighbour == target:
          for counting in closenode:
            count = count + 1
            path += closenode[count-1]+" "
          goal = 1
          print ("BFS Path = " + path)
          print("Path cost = ", count)
          break
    if goal == 1:
      break

  if goal == 0:
    print("Error: the goal node doesn't exist")
 
#DFS 

def dfs(closenode, graph, node, target, opennode):
  path = ""
  count =0
  opennode.append(node)
  if node not in graph:
    print("Error: The start node is not in graph")
  elif target not in graph:
    print("Error: the goal node doesn't exist")
  elif node not in closenode:
        s = opennode.pop(0)
        closenode.append(s)
        if node == target:
          for counting in closenode:
            count = count + 1
            path += closenode[count-1]+" "
          print ("Path = " + path)
          print("Path cost = ", count)
          return
        else:
          for neighbour in graph[node]:
            if neighbour not in closenode:
              dfs(closenode, graph, neighbour, target,opennode)


print("0. BFS\n1. DFS\n")
num=int(input('Enter the choice: '))
print("\n")
if num==0: 
    a = input("Enter the start state: ")
    a = a.upper()
    b = input("Enter the goal state: ")
    b = b.upper()
    bfs(closenode, graph, a, b, opennode)
elif num==1: 
    a = input("Enter the start state: ")
    a = a.upper()
    b = input("Enter the goal state: ")
    b = b.upper()
    dfs(closenode, graph, a, b, opennode)
