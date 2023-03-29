# arr = [1, 2, 0, -1, -1]


# arr.sort()
# n = 0
# z = 0
# p = 0


# def plusemines():

#     for a in range(0, len(arr)):

#         if arr[a] < 0:
#             global n
#             n = n + 1
#         if arr[a] == 0:
#             global z
#             z = z + 1
#         if arr[a] > 0:
#             global p
#             print(arr[a])
#             p = p + 1

#     print(n / (len(arr)), z/(len(arr)), p/(len(arr)), len(arr), n, z, p)


# plusemines()

def plusMinus(arr):
    arr.sort()
    n = 0
    z = 0
    p = 0
    # Write your code here
    for a in range(0, len(arr)):
        if arr[a] < 0:
            n = n + 1
        if arr[a] == 0:
            z = z + 1
        if arr[a] > 0:

            p = p + 1

    print(p/len(arr))
    print(n/len(arr))
    print(z/len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
