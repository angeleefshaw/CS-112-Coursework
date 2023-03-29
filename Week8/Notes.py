# Strings - along with lists are a sequence in Python

# Things in common with lits...
# indexing, slicing, len, looping

# numbers are INTS, damnit
# When you slice a string you always get back a string

# Similar to lists, strings are objects. This means they have built in methods
# However, lists are mutable and strings are immutable

# All string methods returns something since they can't mutate the string
# List methods always returns void (nothing)

# Split method returns a list
string = "83 22 43 1 3 44 32 44"
val = string.split(' ')

# Cast into an int...
for i in range(len(val)):
    val[i] = int(val[i])



wordlist =['L', 'u', 'm', 'b', 'e', 'r', 'j', 'a', 'c', 'k']
wordlist.reverse()
print(wordlist)


word = 'Lumberjack'
print(list(word))

word[0] = 
