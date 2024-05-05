# criteriaMatrix = [[1,5,4,7], [0.2,1,0.5,3], [0.25,2,1,3], [0.14,0.33,0.33,1]]

# criteriaMatrix = [[1,2,2,3,3,0.33,0.33,2,2],
#                   [0.5,1,3,3,3,2,3,2,2],
#                   [0.5,0.33,1,2,2,1,1,2,3],
#                   [0.33,0.33,0.5,1,3,0.33,0.33,1,2],
#                   [0.33,0.33,0.5,0.33,1,0.33,0.33,2,2],
#                   [3,0.5,1,3,3,1,3,2,3],
#                   [3,0.33,1,3,3,0.33,1,2,2],
#                   [0.5,0.5,0.5,1,0.5,0.5,0.5,1,2],
#                   [0.5,0.5,0.33,0.5,0.5,0.33,0.5,0.5,1]]

criteriaMatrix = [[1,2,3,5,7,1/5,8,1/2,1/3],
                  [1/2,1,1/4,1/3,7,1/6,1/2,8,3],
                  [1/3,4,1,1/2,1/3,4,5,1/2,1/3],
                  [1/5,3,2,1,1/7,1/5,5,1/4,8],
                  [1/7,1/7,3,7,1,1/3,4,1/3,8],
                  [5,6,1/4,5,3,1,1/2,1/5,1/7],
                  [1/8,2,1/5,1/5,1/4,2,1,1/3,5],
                  [2,1/8,2,4,3,5,3,1,3],
                  [3,1/3,3,1/8,1/8,7,1/5,1/3,1]]


IRMatrix = [0,0,0,0.58,0.90,1.12,1.24,1.32,1.41,1.45,1.49,1.51,1.48]

def getNormalisedCriteraMatrix(criteriaMatrix):
    n = len(criteriaMatrix)
    sumColumn = [0]*n
    normalisedCriteriaMatrix = []
    for i in range(0, n):
        normalisedCriteriaMatrix.append([0]*n)

    for i in range(0, n):
        for j in range (0, n):
            sumColumn[j]+=criteriaMatrix[i][j]
    
    for i in range(0, n):
        for j in range (0, n):
            normalisedCriteriaMatrix[i][j] = round(criteriaMatrix[i][j]/sumColumn[j], 3)

    return normalisedCriteriaMatrix

def getSynthesisValue(normalisedCriteriaMatrix):
    n = len(normalisedCriteriaMatrix)
    synthesisValue = []

    for i in range(0, n):
        sum = 0
        for j in range (0, n):
            sum+=normalisedCriteriaMatrix[i][j]
        synthesisValue.append(round(sum, 3))

    return synthesisValue

def getEigenValues(criteriaMatrix):
    n = len(criteriaMatrix)
    eigenValues = []

    for i in range(0, n):
        mul = 1
        for j in range (0, n):
            mul = mul*criteriaMatrix[i][j]

        eigenValues.append(round(mul**(1.0/n), 3))
    return eigenValues

def getPriorityWeight(eigenValues):
    n = len(eigenValues)
    priorityWeight = [0]*n
    sum = 0
    for x in eigenValues:
        sum+=x
    
    for i in range(0, n):
        priorityWeight[i] = round(eigenValues[i]/sum, 3)

    return priorityWeight

def getImportanceValue(synthesisValue, priorityWeight):
    n = len(priorityWeight)
    importanceValue = []

    for i in range(0, n):
        importanceValue.append(round(synthesisValue[i]/priorityWeight[i], 3))

    return importanceValue


def calculateCR(importanceValue, IRMatrix):
    total = 0
    n = len(importanceValue)
    for x in importanceValue:
        total = total + x
    
    avg = round(total/n, 3)

    mx = max(importanceValue)
    CI = (avg-n)/(n-1)
    # print(avg)
    CR = CI/IRMatrix[n]
    return CR


normalisedCriteriaMatrix = getNormalisedCriteraMatrix(criteriaMatrix)
n = len(criteriaMatrix)
for i in range(0, n):
    print(normalisedCriteriaMatrix[i])
print(" ")

synthesisValue = getSynthesisValue(normalisedCriteriaMatrix)
print("Synthesis:  "+str(synthesisValue))

eigenValue = getEigenValues(criteriaMatrix)
print("Eigen:  "+str(eigenValue))

priorityWeight = getPriorityWeight(eigenValue)
print("Priority:  "+str(priorityWeight))

importanceValue = getImportanceValue(synthesisValue, priorityWeight)
print("Importance:  "+str(importanceValue))

CR = calculateCR(importanceValue, IRMatrix)

print(CR)


# value of CR is < 0.1 and hence we can say that given weights are consistent

