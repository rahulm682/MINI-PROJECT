from vikor import getEntropyWeight, getRanking

# we will here check for the rank reversal problem by taking different set of alternatives, rank them and check the relative ranking with the initial ranking

def checkForRankReversal(choiceMatrix, criteriaType, v, intialRanking):
    arr = [0]*16
    m = len(choiceMatrix)
    count = 1<<m

    for i in range(count):
        bits = i.bit_count()
        # print(bits, i)
        if bits<2 or bits==m:
            continue

        j = 0
        k = i
        currChoicematrix = []
        while k>0:
            d = k&1
            if d==1:
                currChoicematrix.append(choiceMatrix[j])
            
            j+=1
            k=k>>1

        # print(currChoicematrix)
        a = getEntropyWeight(currChoicematrix)
        entropy = a[0]
        weight = a[1]

        ranking = getRanking(currChoicematrix, criteriaType, weight, v)
        # for i in range(len(ranking)):
        #     print(ranking[i])

        # print("\n")

        l = 0
        r = 0
        with open("rankreversal.txt", "a") as f:
            while l<len(intialRanking) and r<len(ranking):
                if intialRanking[l][0]!=ranking[r][0]:
                    l+=1
                else:
                    r+=1

            if r!=len(ranking):
                for line in ranking:
                    f.write(f"{line}\n")
                f.write("\n\n")
                arr[bits]+=1
            #     for i in range(len(ranking)):
            #         print(ranking[i])

            #     print("\n")

    print(arr)