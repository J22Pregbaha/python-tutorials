def adjacentElementsProduct(inputArray):
    highest_value = []
    for i in range(len(inputArray)):
        if i < len(inputArray) - 1:
            value = inputArray[i] * inputArray[i+1]
        if not highest_value:
            highest_value.append(value)
        else:
            if value > highest_value[0]:
                highest_value.pop()
                highest_value.append(value)
    return highest_value[0]

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
