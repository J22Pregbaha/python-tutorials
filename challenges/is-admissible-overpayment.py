def isAdmissibleOverpayment(prices, notes, x):
    count = 0

    for index, element in enumerate(notes):
        note = element.split()
        if note[1] == "lower":
            percent = float(note[0].replace("%", ""))
            difference = (100 * prices[index])/(100 - percent) - prices[index]
            count -= difference
            # print("lower", (100 * prices[index])/(100 - percent), prices[index], difference)
        elif note[1] == "higher":
            percent = float(note[0].replace("%", ""))
            difference = prices[index] - (100 * prices[index]) / (100 + percent)
            count += difference
            # print("higher", (100 * prices[index]) / (100 + percent), prices[index], difference)

    return count <= x

print(isAdmissibleOverpayment(
    [40, 40, 40, 40],
    ["0.001% higher than in-store",
     "0.0% lower than in-store",
     "0.0% higher than in-store",
     "0.0% lower than in-store"],
    0
))