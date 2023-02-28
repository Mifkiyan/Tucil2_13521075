import math
import random

euclideanCalled = 0

def randomPoint(n, dim):
    arrayPoint = []
    for i in range(0, n):
        point = []
        for j in range(0, dim):
            sumbu = round(random.uniform(-1000, 1000), 2)
            point.append(sumbu)
        arrayPoint.append(point)
    return arrayPoint


def euclideanDistance(point1, point2):
    distance = float(0)
    for i in range(0, len(point1)):
        distance += math.pow((point1[i]-point2[i]), 2)
    global euclideanCalled
    euclideanCalled += 1
    return math.sqrt(distance)


def sortPointbyX(arrayPoint):
    for i in range(0, len(arrayPoint)):
        for j in range(0, len(arrayPoint)-1-i):
            if arrayPoint[j][0] > arrayPoint[j+1][0]:
                arrayPoint[j], arrayPoint[j+1] = arrayPoint[j+1], arrayPoint[j]
    return arrayPoint


def closestPairDivideNConquer(arrayPoint, n, dim):
    if (n == 2):
        distance = euclideanDistance(arrayPoint[0], arrayPoint[1])
        result = [distance, arrayPoint[0], arrayPoint[1]]
        return result
    elif (n == 3):
        d1 = euclideanDistance(arrayPoint[0], arrayPoint[1])
        d2 = euclideanDistance(arrayPoint[0], arrayPoint[2])
        d3 = euclideanDistance(arrayPoint[1], arrayPoint[2])
        if (d1 <= d2) and (d1 <= d3):
            result = [d1, arrayPoint[0], arrayPoint[1]]
        elif (d2 <= d1) and (d2 <= d3):
            result = [d2, arrayPoint[0], arrayPoint[2]]
        else:
            result = [d3, arrayPoint[1], arrayPoint[2]]
        return result
    else:
        mid = n//2
        left = arrayPoint[:mid]
        right = arrayPoint[mid:]

        dleft = closestPairDivideNConquer(left, mid, dim)
        dright = closestPairDivideNConquer(right, n-mid, dim)

        result = []

        if (dleft[0] < dright[0]):
            result = dleft
        else:
            result = dright

        strip = []

        if (n % 2 == 0):
            midPoint = (arrayPoint[mid][0]+arrayPoint[mid+1][0])/2
        else:
            midPoint = arrayPoint[mid][0]

        for i in range(0, n):
            if (arrayPoint[i][0] >= (midPoint - result[0])) and (arrayPoint[i][0] <= (midPoint + result[0])):
                strip.append(arrayPoint[i])

        if (len(strip) > 1):
            for i in range(0, len(strip)):
                for j in range(i+1, len(strip)):
                    found = True
                    for k in range(dim):
                        if found:
                            found = found and (
                                abs(strip[i][k]-strip[j][k]) < result[0])
                    if (found):
                        distance = euclideanDistance(strip[i], strip[j])
                        if (distance < result[0]):
                            result = [distance, strip[i], strip[j]]

        return result


def closestPairBruteForce(arrayPoint, n):
    distance = euclideanDistance(arrayPoint[0], arrayPoint[1])
    result = [distance, arrayPoint[0], arrayPoint[1]]

    for i in range(0, n):
        for j in range(i+1, n):
            temp = euclideanDistance(arrayPoint[i], arrayPoint[j])
            if (temp < distance):
                distance = temp
                result = [distance, arrayPoint[i], arrayPoint[j]]

    return result