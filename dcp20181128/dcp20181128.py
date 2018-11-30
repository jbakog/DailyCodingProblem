# with division
arrayOfInt = [1, 3, 5, 8]
result = []
for outerInt in arrayOfInt:
    mult = 1
    for innerInt in arrayOfInt:
        mult = mult * innerInt
    result.append(int(mult/outerInt))
print(result)

# without division
arrayOfInt = [1, 3, 5, 8]
result = []
for idx, outerInt in enumerate(arrayOfInt):
    mult = 1
    for innerIdx, innerInt in enumerate(arrayOfInt):
        if (idx != innerIdx):
            mult = mult * innerInt
    result.append(int(mult))
print(result)
