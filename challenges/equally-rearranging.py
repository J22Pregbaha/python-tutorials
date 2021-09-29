def equallyRearranging(some):
    newString = ""
    while some != "":
        if "W" in some:
            some = some.replace('W', '', 1)
            newString += "W"
        if "D" in some:
            some = some.replace('D', '', 1)
            newString += "D"
        if "L" in some:
            some = some.replace('L', '', 1)
            newString += "L"

    return newString
print(equallyRearranging("LDWDL"))
