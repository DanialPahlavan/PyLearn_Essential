# get number of sequence from user
n = int(input("How Many Number Fibo want calc?"))
# init
num1 = 0
num2 = 1
temp = num2
print(1, end=" ")

for i in range(n - 1):
    print(temp, end=" ")
    # swap numbers to next number
    num1, num2 = num2, temp
    # make next sequence
    temp = num1 + num2
print()
