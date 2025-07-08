def count_total_characters(*strings):
    total_characters = 0
    for string in strings:
        total_characters += len(string)
    return total_characters


result = count_total_characters("Hello", "world", "!")
print("Total characters:", result)