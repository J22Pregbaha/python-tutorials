def matchingStrings(strings, queries):
    # Write your code here
    output_array = []
    for i in queries:
        count = 0
        for j in strings:
            if i == j:
                count = count + 1
        output_array.append(count)
    return output_array

if __name__ == '__main__':
    strings = ['def', 'de', 'fgh']
    queries = ['de', 'lmn', 'fgh']
    print(matchingStrings(strings, queries))