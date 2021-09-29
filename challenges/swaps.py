lst = [1000, 10, 100]
n = len(lst)
count = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        lst[i], lst[j] = lst[j], lst[i]
        test = lst[:]
        test.sort()
        print(lst)
        if test == lst:
            print(lst)
            count = count + 1

print(count)
if count == 1:
    print("true")
else:
    print("false")
print(n)


