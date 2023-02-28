import math


def euclideanDistance(point1, point2):
    distance = float(0)
    for i in range(len(point1)):
        distance += math.pow((point1[i]-point2[i]), 2)
    return math.sqrt(distance)


def closestPairDivideNConquer(arrayPoint, n):
    if (n == 2):
        distance = euclideanDistance(arrayPoint[0], arrayPoint[1])
        result = [distance, arrayPoint[0], arrayPoint[1]]
        return result
    elif (n == 3):
        d1 = euclideanDistance(arrayPoint[0], arrayPoint[1])
        d2 = euclideanDistance(arrayPoint[0], arrayPoint[2])
        d3 = euclideanDistance(arrayPoint[1], arrayPoint[2])
        if (min(d1, d2, d3) == d1):
            result = [d1, arrayPoint[0], arrayPoint[1]]
        elif (min(d1, d2, d3) == d2):
            result = [d2, arrayPoint[0], arrayPoint[2]]
        else:
            result = [d3, arrayPoint[1], arrayPoint[2]]
        return result
    else:
        mid = n//2
        left = arrayPoint[mid:]
        right = arrayPoint[:mid]

        dleft = closestPairDivideNConquer(left, mid)
        dright = closestPairDivideNConquer(right, n-mid)

        result = []

        if (dleft < dright):
            result = dleft
        else:
            result = dright

        if (n % 2 == 0):
            midPoint = (arrayPoint[mid-1][0]+arrayPoint[mid][0])/2
        else:
            midPoint = arrayPoint[mid][0]


def closestPairBruteForce(arrayPoint):
    distance = euclideanDistance(arrayPoint[0], arrayPoint[1])
    result = [distance, arrayPoint[0], arrayPoint[1]]

    for i in range(len(arrayPoint)):
        for j in range(i+1, len(arrayPoint)):
            temp = euclideanDistance(arrayPoint[i], arrayPoint[j])
            if (temp < distance):
                distance = temp
                result = [distance, arrayPoint[i], arrayPoint[j]]

    return result
