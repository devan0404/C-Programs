word1 = "silent"
word2 = "listen"

a = True
for i in list(word1):
    if i not in list(word2):
        a = False
        break
print("Anagram" if a == True else "Not anagram")

print("Anagram" if sorted(word1) == sorted(word2) else "Not anagram")
