def acronymize():
    full_name = input("Please enter the full name you want to be turned into an acronym: ")
    if full_name:
        name_array = full_name.split()
        acronym = ""

        for word in name_array:
            acronym += word[0]

        print(acronym.upper())
    else:
        print("Please enter a value\n")
        acronymize()

acronymize()