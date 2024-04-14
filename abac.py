from math import pow

def partABAC(decisionMatrix, weights, t, b, criteriaType):
    i = b
    p = t-1
    m = len(decisionMatrix)
    n = len(decisionMatrix[0])

    for k in range(t, b):
        RGik = 1
        RGki = 1

        for j in range(1, n):
            # cost criteria
            if criteriaType[j]:
                RGik = RGik*pow(((decisionMatrix[k][j]+1)/(decisionMatrix[i][j]+1)), weights[j])
                RGki = RGki*pow(((decisionMatrix[i][j]+1)/(decisionMatrix[k][j]+1)), weights[j])
            else:
                RGik = RGik*pow(((decisionMatrix[i][j]+1)/(decisionMatrix[k][j]+1)), weights[j])
                RGki = RGki*pow(((decisionMatrix[k][j]+1)/(decisionMatrix[i][j]+1)), weights[j])

        if RGki>RGik:
            p = p+1
            if p!=k:
                decisionMatrix[p], decisionMatrix[k] = decisionMatrix[k], decisionMatrix[p]


    decisionMatrix[p+1], decisionMatrix[b] = decisionMatrix[b], decisionMatrix[p+1]    

    return p+1


def ABAC(decisionMatrix, weights, t, b, criteriaType):
    if t<b:
        pos = partABAC(decisionMatrix, weights, t, b, criteriaType)
        ABAC(decisionMatrix, weights, t, pos-1, criteriaType)
        ABAC(decisionMatrix, weights, pos+1, b, criteriaType)



__all__ = ('ABAC')