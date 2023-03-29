
# ar1 = [1, 2, 3]
# ar2 = [0, 3, 1]

ar1 = [6, 8, 12]
ar2 = [
    7, 9, 15]

# ar1 = [10, 12, 50]
# ar2 = [20, 20, 10]


def compareTriplets(a, b):
    # Write your code here
    bob = 0
    alice = 0
    if (len(a) != len(b)):
        print("Full Data is required for it")
        return

    for i in range(0, len(a)):
        if a[i] > b[i]:
            alice = alice+1
        if a[i] < b[i]:
            bob = bob+1
        if a[i] == b[i]:
            print("done")

    if bob > alice:
        return bob, alice
    else:
        return alice, bob


result = compareTriplets(ar1, ar2)

print(result)
