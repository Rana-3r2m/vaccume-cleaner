import matplotlib.pyplot as plt
import random

class Node:
    def __init__(self, x,y,name):
        self.x = x
        self.y = y
        self.name = name




matrix = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

_9= Node(3,3,"9")
_8= Node(3,2,"8")
_7= Node(3,1,"7")
_6= Node(2,3,"6")
_5= Node(2,2,"5")
_4= Node(2,1,"4")
_3= Node(1,3,"3")
_2= Node(1,2,"2")
_1= Node(1,1,"1")

nmatrix = [
    [1, 1, 1, 1, 1],
    [1, _1, _2, _3, 1],
    [1, _4, _5, _6, 1],
    [1, _7, _8, _9, 1],
    [1, 1, 1, 1, 1]
]

for mI in range(1, 4):
    for aI in range(1, 4):
        number = random.randint(0, 3)
        if number == 1:
            matrix[mI][aI] = 2

def mapNotClean():
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if (matrix[i][j] == 2):
                return True
    return False

i = random.randint(1, 3)
j = random.randint(1, 3)

initial=nmatrix[i][j]
# print(i," ",j)
list=[]
vlist=[]
dr = [-1, +1, 0, 0]
dc = [0, 0, +1, -1]

list.insert(0,initial)

#to render the matrix when the initial is clean
plt.imshow(matrix, cmap='Blues')
plt.plot(initial.y,initial.x, '*', 4)
plt.pause(.8)
plt.clf()
while (mapNotClean()):
      print(initial.name)
      ######################################
      plt.imshow(matrix, cmap='Blues')
      plt.plot(initial.y,initial.x, '*', 4)
      if matrix[initial.x][initial.y] == 2:
          matrix[initial.x][initial.y] = 0
          print("Clean")
          plt.pause(.8)
      plt.pause(.5)
      plt.clf()

      #####################################
    #   print(list)
      v=list.pop(0)
      vlist.append(v)
      
      for i in range(0,4):
          x = initial.x+dr[i]
          y= initial.y+dc[i]
          
          if x < 1 or y < 1: continue
          if x > 3 or y > 3: continue
        
          n = nmatrix[x][y]
          if (n in vlist): continue
        
          list.insert(0,n)
          
      initial = list[0]

