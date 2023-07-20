import math

def factorsort(array, n):
    def factor_count(num):
        count = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                count += 1
        return count

    for i in range(n - 1):
        for j in range(n - i - 1):
            if factor_count(array[j]) > factor_count(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    factorsort(array, n)
    print(array)
