from vikor import getEntropyWeight, getRanking
from rankreversal import checkForRankReversal

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

# True: Beneficial Criteria, False: Non-Beneficial Criteria 
criteriaType = [True, True, True, True, True, True, True, True, True]
m = len(choiceMatrix)
n = len(choiceMatrix[0])
v = 0.5


a = (getEntropyWeight(choiceMatrix))
entropy = a[0]
weight = a[1]

# print("\n\nEntropy: ")
# for j in range(n):
#     print(round(entropy[j], 3), end=" ")

# print("\n\nWeight:")
# for j in range(n):
#     print(round(weight[j], 3), end=" ")


ranking = getRanking(choiceMatrix, criteriaType, weight, v)
for i in range(m):
    print(ranking[i])

checkForRankReversal(choiceMatrix, choiceMatrix, v, ranking)