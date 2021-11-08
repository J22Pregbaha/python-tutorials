def reverseDigitsInPairs(n):
    n = str(n)
    odd = []
    even = []

    for i in range(len(n)):
        if i % 2 != 0:
            odd.append(n[i])
        else:
            even.append(n[i])

    final_string = ""
    for i in range(max(len(even), len(odd))):
        if i < len(odd):
            final_string += odd[i]
        if i < len(even):
            final_string += even[i]

    return int(final_string)

print(reverseDigitsInPairs(72328))