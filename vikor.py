from math import log2, sqrt

# first of all we need to calculate weight and entropy for the given set of alternatives criteria
def getEntropyWeight(choiceMatrix):
    m = len(choiceMatrix)
    n = len(choiceMatrix[0])

    # summation dij for each column
    sumForColumn = []
    for j in range(n):
        sum = 0
        for i in range(m):
            sum+=choiceMatrix[i][j]
        sumForColumn.append(sum)

    # normalised Matrix for calculation of entropy and entropy weight for each criteria 
    normalisedMatrix = []
    for i in range(m):
        currRow = []
        for j in range(n):
            currRow.append(choiceMatrix[i][j]/sumForColumn[j])
        
        normalisedMatrix.append(currRow)


    # entropy and degree of differentiation(f)
    entropy = []
    f = []
    for j in range(n):
        e = 0
        for i in range(m):
            e -= normalisedMatrix[i][j]*log2(normalisedMatrix[i][j])/log2(m)
        
        entropy.append(e)
        f.append(1-e)


    # calculation of weight for each criteria, for that we need sum of f and weight of jth criteria = f(j)/sum of f
    sumF = 0
    for x in f:
        sumF+=x

    weight = []
    for x in f:
        weight.append(x/sumF)

    # print(normalisedMatrix)
    # print("\n\nEntropy: ")
    # for j in range(n):
        # print(round(entropy[j], 3), end=" ")

    # print("\n\nWeight:")
    # for j in range(n):
    #     print(round(weight[j], 3), end=" ")

    return entropy, weight



# get ranking of the alternatives using the choiceMatrix, criteria weight, criteria type and weight v=0.5
def getRanking(choiceMatrix, criteriaType, weight, v):
    m = len(choiceMatrix)
    n = len(choiceMatrix[0])
    
    # we will calculate the normalised matrix for the VIKOR method
    # for that we will be needing first the root of sum of squares of values present in each column (i.e. c(ij) = d(ij)/sqrt(sum of square of each values in column))
    rootValues = []
    normalisedDecisionMatrix = []

    for j in range(n):
        sum = 0
        for i in range(m):
            sum+=choiceMatrix[i][j]*choiceMatrix[i][j]
        rootValues.append(sqrt(sum))

    for i in range(m):
        currRow = []
        for j in range(n):
            currRow.append(choiceMatrix[i][j]/rootValues[j])
        
        normalisedDecisionMatrix.append(currRow)

    # print("\n\nNormalised Decision Matrix: \n\n")
    # for i in range(m):
    #     for j in range(n):
    #         print(round(normalisedDecisionMatrix[i][j], 3), end=" ")
    #     print()


    # for calculation of utility and regret measures S and R, we will need max and min values from each column and store them
    maxColumn = []
    minColumn = []

    for j in range(n):
        minV = 1e9+7
        maxV = -1e9+7
        for i in range(m):
            maxV = max(normalisedDecisionMatrix[i][j], maxV)
            minV = min(normalisedDecisionMatrix[i][j], minV)
        
        maxColumn.append(maxV)
        minColumn.append(minV)


    # printing max and min value
    # print("\n\nminValue: ")
    # for i in range(n):
    #     print(round(minColumn[i], 3), end=" ")

    # print("\n\nmaxvalue: ")
    # for i in range(n):
    #     print(round(maxColumn[i], 3), end=" ")

    # print("\n\n")

    # Calculate Utility Value S
    s = []
    for i in range(m):
        sum = 0
        for j in range(n):
            if maxColumn[j]-minColumn[j]==0:
                maxV = float('inf')
            elif criteriaType[j]:
                sum += weight[j]*(maxColumn[j]-normalisedDecisionMatrix[i][j])/(maxColumn[j]-minColumn[j])
            else:
                sum += weight[j]*(normalisedDecisionMatrix[i][j]-minColumn[j])/(maxColumn[j]-minColumn[j])

        s.append(sum)

    # Calculate Regret value R
    r = []
    for i in range(m):
        maxV = 0
        for j in range(n):
            if maxColumn[j]-minColumn[j]==0:
                maxV = float('inf')
            elif criteriaType[j]:
                maxV = max(maxV, weight[j]*(maxColumn[j]-normalisedDecisionMatrix[i][j])/(maxColumn[j]-minColumn[j]))
            else:
                maxV = max(maxV, weight[j]*(normalisedDecisionMatrix[i][j]-minColumn[j])/(maxColumn[j]-minColumn[j]))
        
        r.append(maxV)


    # print("\n\nUtiltiy Values R ans S\n\n")
    # for j in range(m):
    #     print(round(s[j], 3), end=" ")

    # print()

    # for j in range(m):
    #     print(round(r[j], 3), end=" ")

    # print()


    # calculate VIKOR index
    mins = min(s)
    maxs = max(s)

    minr = min(r)
    maxr = max(r)
    v = 0.5

    q = []
    for i in range(m):
        currQ = v*(s[i]-mins)/(maxs-mins) + (1-v)*(r[i]-minr)/(maxr-minr)
        q.append(currQ)

    # print("\n\nVIKOR Index: ")
    # for j in range(m):
    #     print(round(q[j], 3), end=" ")

    # print()


    # storing all values in matrix and sorting the values according to the Q values
    ranking = []
    for i in range(m):
        curr = [i+1, round(s[i], 3), round(r[i], 3), round(q[i], 3)]
        ranking.append(curr)

    ranking = sorted(ranking, key=lambda l:l[3])

    # for i in range(m):
    #     print(ranking[i])

    return ranking

__all__ = ('getEntropyWeight', 'getRanking')