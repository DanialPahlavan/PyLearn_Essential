# delete repetive item of a list

# init
SampleList = [1, 2, 2, 6, 5, 6]
NonRepitiveSampleList = []
RepitiveCounter = 0
RepitiveFound = False

for i in SampleList:
    for j in SampleList:
        if i == j:
            RepitiveCounter += 1
            if RepitiveCounter > 1:
                RepitiveFound = True
    if RepitiveFound == False:
        NonRepitiveSampleList.append(i)

    RepitiveCounter = 0
    RepitiveFound = False

print("Main List =", SampleList)
print("Clean Repeative List", NonRepitiveSampleList)
