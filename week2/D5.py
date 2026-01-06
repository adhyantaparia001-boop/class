
def is_palindrome(string):
    if string.lower().strip() == string.lower().strip()[-1]:
        return True
    else:
        return False
print(is_palindrome('abd'))
vowels=['a','e','i','o','u']

def count_vowles(string):
    vowelss= {}
    stringg = string.lower().strip()

    for character in stringg:
        if character in vowels:
            if character in vowelss:
                vowelss[character]+=1
            else:
                vowelss[character]=1

        return vowelss

print(count_vowles('abdaa ee ii oofkdbs dfj'))

