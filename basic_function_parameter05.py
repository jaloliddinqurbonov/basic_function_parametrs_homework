# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def count_vowels(l):
    a=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s=0
    for i in l:
        if i in a:
            s+=1
    return s
print(count_vowels('dnjndevnDEVNOrwvj'))

