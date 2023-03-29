number = int(input("enter the value to check for prime: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("This is not a prime number")
            print(i, "times", number//i, "is", number)
            break
    else:
        print(f"Yes {number} is a prime number")
