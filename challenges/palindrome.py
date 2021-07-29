print("Hi there, I'm a palindrome checker.\nHere's how it works. You'll give me 5 words/phrases and I'll tell you which ones are palindromes")

def words():
    first_word = input("First word/phrase: ")
    if first_word:
        second_word = input("Second word/phrase: ")
        if second_word:
            third_word = input("Third word/phrase: ")
            if third_word:
                fourth_word = input("Fourth word/phrase: ")
                if fourth_word:
                    fifth_word = input("Fifth word/phrase: ")
                    if fifth_word:
                        all_words = [first_word, second_word, third_word, fourth_word, fifth_word]
                        checker(all_words)
                    else:
                        reset()
                else:
                    reset()
            else:
                reset()
        else:
            reset()
    else:
        reset()

def checker(all_words):
    count = 0
    for word in all_words:
        reversed_word = word[::-1]
        if reversed_word == word:
           count += 1
    print("Out of your five words,", count, "are palindromes")

def reset():
    print("Nope")
    words()

words()