import ClosestPair as util
import time
import platform

dim = int(input("Masukkan banyak dimensi : "))

while dim < 2:
    print("Masukan tidak valid. Dibutuhkan minimal 2 dimensi\n")
    dim = int(input("Masukkan banyak dimensi : "))

n = int(input("Masukkan banyak titik : "))

while n < 2:
    print("Masukan tidak valid. Dibutuhkan minimal 2 titik untuk menghitung jarak\n")
    n = int(input("Masukkan banyak titik : "))

arrayPoint = util.randomPoint(n, dim)
arrayPoint = util.sortPointbyX(arrayPoint)

startDnC = time.time()
resultDnC = util.closestPairDivideNConquer(arrayPoint, n, dim)
timeDnC = time.time() - startDnC
euclideanDnC = util.euclideanCalled

startBF = time.time()
resultBF = util.closestPairBruteForce(arrayPoint, n)
timeBF = time.time() - startBF
euclideanBF = util.euclideanCalled - euclideanDnC


print("\n=================== DIVIDE AND CONQUER ===================")
print("Point 1                :", resultDnC[1])
print("Point 2                :", resultDnC[2])
print("Distance between them  :", resultDnC[0])
print("Execution time         :", timeDnC, "s")
print("Euclidean function is called", str(euclideanDnC) + "x\n")


print("====================== BRUTE FORCE =======================")
print("Point 1                :", resultBF[1])
print("Point 2                :", resultBF[2])
print("Distance between them  :", resultBF[0])
print("Execution time         :", timeBF, "s")
print("Euclidean function is called", str(euclideanBF) + "x\n")

print("Run at", platform.platform(), platform.processor(), platform.machine())
