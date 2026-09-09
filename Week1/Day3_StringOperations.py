def str_length(word):
    return len(word)
def str_lowercase(word):
    return word.lower()
def str_uppercase(word):
    return word.upper()
def str_rev(word):
    return word[::-1]

def vowel_count(word):
    v = 'aeiou'
    c=0
    for i in word.lower():
        if i in v:
            c+=1
    return c
    
word = input()
print("String Length:", str_length(word))
print("Lower case: ", str_lowercase(word))
print("Upper case: ", str_uppercase(word))
print("Reversed String: ", str_rev(word))
print("Vowel Count: ", vowel_count(word))
