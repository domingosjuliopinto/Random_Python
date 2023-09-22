import math
 
def minimax (curDepth, nodeIndex,maxTurn, scores,targetDepth):
 

    if (curDepth == targetDepth):
        return scores[nodeIndex]
     
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 3,    False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 3 + 1,False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 3 + 2,False, scores, targetDepth))
     
    else:
        return min(minimax(curDepth + 1, nodeIndex * 3,    True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 3 + 1,True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 3 + 2,True, scores, targetDepth))
     

scores = []

x=int(input("Enter total number of leaf nodes ="))
for i in range(x):
    y=int(input("Enter leaf "+str(i+1)+" values: "))
    scores.append(y)

 
treeDepth = math.log(len(scores), 3)
 
print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))
