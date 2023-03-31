
def space(n):
    spa = ''
    for i in range(0, n-1):
        spa = spa+"0"
    return spa


def staircase(n):
    s = ""
    for i in range(n):
        for k in range(n):
            if k < n-i-1:
                s = s+" "
            else:
                s = s+"#"
        s = s+"\n"
    print(s)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
