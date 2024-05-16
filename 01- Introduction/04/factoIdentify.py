# identify facto or not

FactResultNumber = int(input("Fact Result Number: [example 24 => that is 4!]"))

number = FactResultNumber
FactNumberList = []
i = 1

# Find Seq of Number
while FactResultNumber != 1 and i <= number:
    if FactResultNumber % i == 0:
        FactResultNumber //= i
        FactNumberList.append(i)
    i += 1

# Check Fact or Not
if FactResultNumber == 1:
    print("Your number is a factorial of", i - 1)
    print(i - 1, "!=", end=" ")
    for NumberOfMulti in FactNumberList:
        print(NumberOfMulti, end=" * " if NumberOfMulti != FactNumberList[-1] else "")
    print(" =", number)
else:
    print("It's Not Fact")
