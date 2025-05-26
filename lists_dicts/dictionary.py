user_str = input(str("Enter something: "))

word_dict = {"hola": "Hi", "amigo": "friend", "que": "what", "universidad": "university"}

listed_words = user_str.split()

translation_list  = []

for word in listed_words:
    if word in word_dict:
        translation_list.append(word_dict[word])
    else:
        translation_list.append(word)

final_word = ' '.join(translation_list)
print(final_word)


