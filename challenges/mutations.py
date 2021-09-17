"""Return true if the string in the first element of the array contains all of the letters of the string in the second element of the array"""

def mutate(array):
    first_word = str.lower(array[0])
    words = len(array)
    not_found = 0
    for i in range(1, words):
        for letter in array[i]:
            if not str.lower(letter) in first_word:
                not_found = not_found + 1
    if not_found > 0:
        print("false")
    else:
        print("true")

mutate(["hello", "Hello", "lehol"])

"""I went a step further to check if all the words have letters that can be found in the first word in the array"""