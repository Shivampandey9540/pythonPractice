def diagonalDifference(arr, ):

    # Write your code here
    leftdig = 0
    rightdig = 0
    # print(len(arr))
    for a in range(len(arr)):
        for b in range(len(arr[a])):
            if b == (len(arr)-a - 1):
                print("heelo", arr[a][b])
                rightdig = rightdig + arr[a][b]
            if a == b:
                leftdig = leftdig + arr[a][b]

    # if leftdig < 0:
    #     leftdig = leftdig * -1
    # if rightdig < 0:
    #     rightdig = rightdig * -1
    answer = leftdig - rightdig
    if answer < 0:
        answer = answer * -1
    print(answer)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    diagonalDifference(arr)
