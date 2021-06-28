import random

class NearestNeighbour:
  def __init__(self, graph):
    super().__init__()
    assert isinstance(graph, dict), f'Graph should be a dictionary instead of ${type(graph)}'
    self.graph = graph
    self.current = {}
    self.visitedKeys = []
    self.distance = 0
    self.shortestPath()
    self.printPath()

  def pickStartVert(self):
    assert len(self.graph) > 2, f'Graph should contain at least 2 vertices, it contains ${len(self.graph)}'
    startVertIndex = random.choice(list(self.graph.keys()))
    current = self.graph[startVertIndex]
    self.visit(startVertIndex)
    return current

  def shortestEdge(self):
    shortestVertex = {}
    for nextVertex in self.current:
      if not(nextVertex['key'] in self.visitedKeys) and (len(shortestVertex) < 1 or nextVertex['distance'] < shortestVertex['distance']):
        shortestVertex = nextVertex
    return shortestVertex;
      
  def shortestPath(self):
    self.current = self.pickStartVert()
    while len(self.visitedKeys) < len(self.graph):
      nextVertice = self.shortestEdge() 
      if len(nextVertice) > 0:
        self.distance += nextVertice['distance']  
        self.current = self.graph[nextVertice['key']] 
        self.visit(nextVertice['key'])
      else:
        break  

      
  def visit(self, key):
    self.visitedKeys.append(key)

  def printPath(self):
    print(f'Shortest path: {self.visitedKeys} \nTotal Distance: {self.distance}')

# Graph Link: https://i.imgur.com/Pt080Op.png
graph = {'A': [{
    'key': 'B',
    'distance': 3
  }, {
    'key': 'C',
    'distance': 4
  }],
  'B': [{
    'key': 'A',
    'distance': 3
  }, {
    'key': 'I',
    'distance': 11
  }, {
    'key': 'E',
    'distance': 7
  }, {
    'key': 'H',
    'distance': 10
  }], 
  'C': [{
    'key': 'D',
    'distance': 7
  }, {
    'key': 'F',
    'distance': 9
  }],
  'D': [{
    'key': 'C',
    'distance': 7
  }, {
    'key': 'E',
    'distance': 9
  }],
  'E': [{
    'key': 'B',
    'distance': 7
  }, {
    'key': 'D',
    'distance': 9
  }, {
    'key': 'F',
    'distance': 11
  }, {
    'key': 'H',
    'distance': 13
  }],
  'F': [{
    'key': 'C',
    'distance': 9
  }, {
    'key': 'E',
    'distance': 11
  }, {
    'key': 'G',
    'distance': 13
  }],
  'G': [{
    'key': 'F',
    'distance': 13
  }, {
    'key': 'H',
    'distance': 15
  }, {
    'key': 'K',
    'distance': 18
  }],
  'H': [{
    'key': 'B',
    'distance': 10
  }, {
    'key': 'E',
    'distance': 13
  }, {
    'key': 'G',
    'distance': 15
  }, {
    'key': 'J',
    'distance': 18
  }, {
    'key': 'K',
    'distance': 19
  }, {
    'key': 'L',
    'distance': 20
  }],
  'I': [{
    'key': 'B',
    'distance': 11
  }, {
    'key': 'J',
    'distance': 19
  }],
  'J': [{
    'key': 'H',
    'distance': 18
  }, {
    'key': 'I',
    'distance': 19
  }], 
  'K': [{
    'key': 'G',
    'distance': 18
  }, {
    'key': 'H',
    'distance': 19
  }], 
  'L': [{
    'key': 'H',
    'distance': 20
  }]}

NearestNeighbour(graph)