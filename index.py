from math import pow
from abac import ABAC
from vikor import getEntropyWeight

# ranking using entropy weight and ABAC

decisionMatrix = [
    [1, 14.15, 10.00, 4.00, 3250, 5500, 1300, 15240, 1840, 10211], 
    [2, 23.00, 15.00, 5.00, 17600, 77162, 1305, 18000, 3400, 18288],
    [3, 13.20, 8.20, 4.40, 22700, 36000, 2205, 15250, 1000, 13716],
    [4, 22.60, 14.20, 5.90, 18500, 26000, 2400, 20000, 5500, 21031],
    [5, 15.50, 8.00, 4.08, 9700, 9000, 1500, 15000, 2000, 7620],
    [6, 16.80, 11.20, 4.80, 10000, 23000, 2500, 19800, 3800, 18288],
    [7, 18.92, 13.56, 5.02, 14514, 24947, 2574, 15240, 3218, 21000],
    [8, 15.37, 10.65, 5.28, 13155, 31800, 1930, 15240, 2220, 12190],
    [9, 19.81, 13.87, 5.00, 14000, 25500, 2350, 20000, 3000, 13868],
    [10, 14.20, 9.10, 4.50, 8900, 13000, 2570, 15250, 750, 13716],
    [11, 20.60, 13.30, 4.30, 13100, 23330, 2335, 19800, 4500, 18000],
    [12, 14.00, 10.00, 4.00, 3200, 5000, 1200, 15000, 1750, 10058],
    [13, 15.00, 10.00, 5.00, 16400, 23400, 1300, 18000, 4000, 21336],
    [14, 22.00, 14.20, 6.05, 18500, 37000, 2600, 20000, 5000, 361],
    [15, 19.00, 13.50, 5.00, 14150, 27215, 2400, 20000, 3200, 15240]
    ]

# decisionMatrix = [
#     [1, 0.29, 92.89, 126.66, 110.33, 104],
#     [2, 0.42, 119.63, 111.95, 100.5, 131.81],
#     [3, 0.45, 29.07, 152.96, 42.47, 90.83],
#     [4, 0.42, 74.53, 6.19, 130.84, 90.37],
#     [5, 0.48, 96, 140.89, 133, 70.91], 
#     [6, 0.9, 100.15, 81.21, 78.66, 70.90],
#     [7, 1.05, 81.22, 58.42, 68.45, 78.15],
#     [8, 0.56, 43.02, 17.34, 141.23, 51.71],
#     [9, 0.34, 64.64, 75.89, 174.12, 100.14],
#     [10, 0.48, 130.68, 23.2, 122.62, 89.74]
# ]

# currChoiceMatrix = [decisionMatrix[1], decisionMatrix[5], decisionMatrix[3]]

# criteriaType = [True, True, True, False, False, False]
# weights = [0, 0.1625, 0.1072, 0.3483, 0.1356, 0.2464]
# True: Cost Criteria, False: Beneficial Criteria and here 1-based Indexing used
criteriaType = [True, False, False, False, False, False, False, False, False, False]

a = (getEntropyWeight(decisionMatrix))
weights = a[1]

m = len(decisionMatrix)
ABAC(decisionMatrix, weights, 0, m-1, criteriaType)

for i in range (0, m):
    print(decisionMatrix[i])

print("\n\n")

# ABAC(currChoiceMatrix, weights, 0, 2, criteriaType)
# for i in range(0, 3):
#     print(currChoiceMatrix[i])

# print(pow(2, 3.3))