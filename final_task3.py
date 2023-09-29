def middle_characters(word):
   
    if len(word) % 2 == 0:
        middle1 = word[len(word)// 2 - 1]
        middle2 = word[len(word) // 2]
        return middle1 + middle2
    else:
        middle = word[len(word) // 2]
        return middle

input_word = input("Enter a word: ")
result = middle_characters(input_word)
print("Middle :", result)
