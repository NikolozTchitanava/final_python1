def count_duplicate_characters(input_string):
   
    input_string = input_string.lower()

    char_count = {}

    for char in input_string:
       
        if char.isalnum():
          
            char_count[char] = char_count.get(char, 0) + 1

    count = sum(1 for char, freq in char_count.items() if freq > 1)

    return count

input_string = input("Enter a string: ")
result = count_duplicate_characters(input_string)
print("number of cherecters that occur more than once", result)
