
def sort_words(input_string):
    words = input_string.split()
    words.sort()
    return words

input_string = input("Enter a string: ")
sorted_words = sort_words(input_string)
print("Sorted words:", sorted_words)
