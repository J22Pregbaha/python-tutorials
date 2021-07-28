preference = input("Hi there! Would you like to tell me what's on your mind or do you have it already typed out? \nEnter 'n' for a text file or 'o' if you have it typed out\n")
if preference:
    if preference == "n":
        text_file = input("Please enter your filename: ")
        f = open(text_file, "r")
        text = f.read()
        f.close() # It is a good practice to always close the file when you are done with it.
    elif preference == "o":
        text = input("Hi there. What's on your mind today? ")
else:
    print("Please provide an input\n")

text_array = text.split()
print("Oh nice, you just told me what's on your mind in", len(text_array), "words!")