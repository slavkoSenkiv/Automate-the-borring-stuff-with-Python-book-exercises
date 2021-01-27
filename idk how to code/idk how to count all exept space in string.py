"""The setdefault() method is a nice shortcut to ensure that a key exists.
Here is a short program that counts the number of occurrences of each
letter in a string."""


# how to skip space counting
message = 'a bb ccc a b c '
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
