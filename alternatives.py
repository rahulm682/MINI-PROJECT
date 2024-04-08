# This clacuation is for calculating the entropy and then using the entropy we are finding the degree of Differentiation and entropy weight for each criteria

from math import log2, sqrt

n = 9
m = 15

# True: Beneficial Criteria, False: Non-Beneficial Criteria 
criteriaType = [True, True, True, True, True, True, True, True, True]

choiceMatrix = [
    [14.15, 10.00, 4.00, 3250, 5500, 1300, 15240, 1840, 10211], 
    [23.00, 15.00, 5.00, 17600, 77162, 1305, 18000, 3400, 18288],
    [13.20, 8.20, 4.40, 22700, 36000, 2205, 15250, 1000, 13716],
    [22.60, 14.20, 5.90, 18500, 26000, 2400, 20000, 5500, 21031],
    [15.50, 8.00, 4.08, 9700, 9000, 1500, 15000, 2000, 7620],
    [16.80, 11.20, 4.80, 10000, 23000, 2500, 19800, 3800, 18288],
    [18.92, 13.56, 5.02, 14514, 24947, 2574, 15240, 3218, 21000],
    [15.37, 10.65, 5.28, 13155, 31800, 1930, 15240, 2220, 12190],
    [19.81, 13.87, 5.00, 14000, 25500, 2350, 20000, 3000, 13868],
    [14.20, 9.10, 4.50, 8900, 13000, 2570, 15250, 750, 13716],
    [20.60, 13.30, 4.30, 13100, 23330, 2335, 19800, 4500, 18000],
    [14.00, 10.00, 4.00, 3200, 5000, 1200, 15000, 1750, 10058],
    [15.00, 10.00, 5.00, 16400, 23400, 1300, 18000, 4000, 21336],
    [22.00, 14.20, 6.05, 18500, 37000, 2600, 20000, 5000, 361],
    [19.00, 13.50, 5.00, 14150, 27215, 2400, 20000, 3200, 15240]
    ]

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


entropy = []
# degree of differentiation (f)
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
print("\n\nEntropy: ")
for j in range(n):
    print(round(entropy[j], 3), end=" ")

print("\n\nWeight:")
for j in range(n):
    print(round(weight[j], 3), end=" ")




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

print("\n\nNormalised Decision Matrix: \n\n")
for i in range(m):
    for j in range(n):
        print(round(normalisedDecisionMatrix[i][j], 3), end=" ")
    print()


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
print("\n\nminValue: ")
for i in range(n):
    print(round(minColumn[i], 3), end=" ")

print("\n\nmaxvalue: ")
for i in range(n):
    print(round(maxColumn[i], 3), end=" ")

print("\n\n")

# Calculate Utility Value S
s = []
for i in range(m):
    sum = 0
    for j in range(n):
        if criteriaType[j]:
            sum += weight[j]*(maxColumn[j]-normalisedDecisionMatrix[i][j])/(maxColumn[j]-minColumn[j])
        else:
            sum += weight[j]*(normalisedDecisionMatrix[i][j]-minColumn[j])/(maxColumn[j]-minColumn[j])

    s.append(sum)

# Calculate Regret value R
r = []
for i in range(m):
    maxV = 0
    for j in range(n):
        if criteriaType[j]:
            maxV = max(maxV, weight[j]*(maxColumn[j]-normalisedDecisionMatrix[i][j])/(maxColumn[j]-minColumn[j]))
        else:
            maxV = max(maxV, weight[j]*(normalisedDecisionMatrix[i][j]-minColumn[j])/(maxColumn[j]-minColumn[j]))
    
    r.append(maxV)


print("\n\nUtiltiy Values R ans S\n\n")
for j in range(m):
    print(round(s[j], 3), end=" ")

print()

for j in range(m):
    print(round(r[j], 3), end=" ")

print()


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

print("\n\nVIKOR Index: ")
for j in range(m):
    print(round(q[j], 3), end=" ")

print()


# storing all values in matrix and sorting the values according to the Q values
ranking = []
for i in range(m):
    curr = [i+1, round(s[i], 3), round(r[i], 3), round(q[i], 3)]
    ranking.append(curr)

ranking = sorted(ranking, key=lambda l:l[3])

for i in range(m):
    print(ranking[i])