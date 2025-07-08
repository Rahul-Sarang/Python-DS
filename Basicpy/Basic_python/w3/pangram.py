text = input("Enter a string: ")
text = text.lower()
a = dict()

for i in text:
    if i != ' ':
        a[i] = a.get(i, 0) + 1

if len(a.keys()) == 26:
    print("String is a Pangram")
else:
    print("String is not a Pangram")
