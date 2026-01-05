import numbers

vowels = ('a','e','i','o','u')

def vowels_count(word):
     count = 0
     for char in word:
         if char.lower() not in vowels:
             count+=1
     return count

print(vowels_count('apple'))
def min_max(arr) :
    min = arr[0]
    max = arr[0]
    for item in arr :
        if item < min :
            min = item
        if item > max :
            max = item
    return min, max
print(min_max([1,4,7,6,8,9]))
def remove_duplicates (dupli):
    dupes = []
    for item in dupli :

        if item not in dupes :
            dupes.append(item)

    return dupes
print(remove_duplicates([1,1,2,2,3,4,5,6,7,8,9]))
