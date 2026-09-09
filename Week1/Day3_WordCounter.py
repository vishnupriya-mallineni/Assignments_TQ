text = input()
words = text.split(" ")
print("Number of words:", len(words))
print("Lengths of each word:")
for i in words:
    print(len(i))
