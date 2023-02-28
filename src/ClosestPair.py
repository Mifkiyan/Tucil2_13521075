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

        if (dleft[0] < dright[0]):
            result = dleft
        else:
            result = dright

        strip = []

        if (n % 2 == 0):
            midPoint = (arrayPoint[mid-1][0]+arrayPoint[mid][0])/2
        else:
            midPoint = arrayPoint[mid][0]

        for i in range(len(arrayPoint)):
            if (arrayPoint[i][0] >= midPoint - result[0]) and (arrayPoint[i][0] <= midPoint + result[0]):
                strip.append(arrayPoint[i])

        a = 0
        b = 1
        distance = euclideanDistance(strip[a], strip[b])
        for i in range(len(strip)):
            for j in range(i+1, len(strip)):
                temp = euclideanDistance(strip[i], strip[j])
                if (temp < distance):
                    distance = temp
                    a = i
                    b = j

        if (distance < result[0]):
            result = [distance, strip[a], strip[b]]

        return result


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
