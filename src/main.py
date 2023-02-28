import ClosestPair as util
import time
import random

n = int(input("Masukkan banyak titik : "))

while n < 2:
    print("Masukan tidak valid. Dibutuhkan minimal 2 titik untuk menghitung jarak\n")
    n = int(input("Masukkan banyak titik : "))
