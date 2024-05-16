# Least common multiple(GCD)

# Get numbers
NumA = int(input("Number 1:"))
NumB = int(input("Number 2:"))

# init
MultA = []
MultB = []
GCD = 0
FoundLCM = False
# Find coefficients
for i in range(2, NumA):
    if NumA % i == 0:
        MultA.append(i)
for j in range(2, NumB):
    if NumB % j == 0:
        MultB.append(j)
print(MultA)
print(MultB)

# search between coefficients - GCD

for i in MultA:
    for j in MultB:
        if i == j:
            if i > GCD:
                GCD = i

if not GCD:
    print("Not Found")
else:
    print("GCD:", GCD)
