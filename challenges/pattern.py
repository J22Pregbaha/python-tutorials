# You are given two strings pattern and s. The first string pattern contains only the symbols 0 and 1, and the second string s contains only lowercase English letters.
#
# Let's say that pattern matches a substring s[l..r] of s if the following 3 conditions are met:
#
# they have equal length;
# for each 0 in pattern the corresponding letter in the substring is a vowel;
# for each 1 in pattern the corresponding letter is a consonant.
# Your task is to calculate the number of substrings of s that match pattern.
#
# Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'. All other letters are consonants.
#
# Example
#
# For pattern = "010" and s = "amazing", the output should be solution(pattern, s) = 2.
# "010" matches s[0..2] = "ama", because both 0s match a, which is a vowel, and 1 match m, which is a consonant;
# "010" doesn't match s[1..3] = "maz", because the first 0 corresponds to an m, which is a consonant, not a vowel;
# "010" matches s[2..4] = "azi", because the first 0 matches an a (vowel), 1 matches z (consonant), and the second 0 matches i (vowel);
# "010" doesn't match s[3..5] = "zin", because the first 0 corresponds to a consonant (z);
# "010" doesn't match s[4..6] = "ing", because the second 0 corresponds to the letter g, which is a consonant.
# So, there are only 2 matches.
def solution(pattern, s):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "y"]
    for i in range(len(s)):
        mill = 0
        if i < len(s) - (len(pattern) - 1):
            for j in range(len(pattern)):
                if pattern[j] == "0" and s[i + j] in vowels:
                    mill += 1
                elif pattern[j] == "1" and s[i + j] not in vowels:
                    mill += 1
        if mill == len(pattern):
            count += 1

    return count

print(solution("00", "aaaaaaaaaa"))