
lower_range = int(input("Enter the lower boundary: "))
upper_range = int(input("Enter the upper boundart: "))
# number = 7
for number in range(lower_range, upper_range+1):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not a prime")
                break
        else:
            print(f"{number} is prime")
