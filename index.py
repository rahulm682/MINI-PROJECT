from math import pow
from abac import ABAC

decisionMatrix = [
    [1, 0.29, 92.89, 126.66, 110.33, 104],
    [2, 0.42, 119.63, 111.95, 100.5, 131.81],
    [3, 0.45, 29.07, 152.96, 42.47, 90.83],
    [4, 0.42, 74.53, 6.19, 130.84, 90.37],
    [5, 0.48, 96, 140.89, 133, 70.91], 
    [6, 0.9, 100.15, 81.21, 78.66, 70.90],
    [7, 1.05, 81.22, 58.42, 68.45, 78.15],
    [8, 0.56, 43.02, 17.34, 141.23, 51.71],
    [9, 0.34, 64.64, 75.89, 174.12, 100.14],
    [10, 0.48, 130.68, 23.2, 122.62, 89.74]
]

currChoiceMatrix = [decisionMatrix[1], decisionMatrix[5], decisionMatrix[3]]

criteriaType = [True, True, True, False, False, False]
weights = [0, 0.1625, 0.1072, 0.3483, 0.1356, 0.2464]

m = len(decisionMatrix)
ABAC(decisionMatrix, weights, 0, m-1, criteriaType)

for i in range (0, m):
    print(decisionMatrix[i])

print("\n\n")

# ABAC(currChoiceMatrix, weights, 0, 2, criteriaType)
# for i in range(0, 3):
#     print(currChoiceMatrix[i])

# print(pow(2, 3.3))