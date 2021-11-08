def romanToInt(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val

def romanToIntTwo(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom_dub_val = {'IV': 4, 'IX': 9, 'CM': 900, 'XC': 90}
    doubles = ['IV', 'IX', 'CM', 'XC']
    singles = []
    mixed = []
    for i in range(len(s)):
        if i > 0 and len(singles) > 0:
            if singles[-1] + s[i] in doubles:
                mixed.append(singles[-1] + s[i])
                singles.pop()
            else:
                singles.append(s[i])
        else:
            singles.append(s[i])

    int_val = 0
    if singles:
        for i in singles:
            int_val += rom_val[i]


    if mixed:
        for i in mixed:
            int_val += rom_dub_val[i]

    return int_val

print(romanToInt("MCMXCIV")) # From Discussions
print(romanToIntTwo("MCMXCIV")) # Mine. Implemented with stacks