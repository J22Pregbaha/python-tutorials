# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
def addBorder(picture):
    final_array = []
    length = len(picture[0])
    asterisks = "*" * length + "**"
    final_array.append(asterisks)

    for i in picture:
        if set(i) != "*":
            final_array.append("*" + i + "*")
        else:
            final_array.append(asterisks)

    final_array.append(asterisks)

    return final_array

print(addBorder(["abc", "ded"]))