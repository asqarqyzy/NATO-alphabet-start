import pandas as pd
#TODO 1. Create a dictionary in this format:
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

# for (key, value) in nato_data.iterrows():
#     print(value.letter, value.code)
#     break
nato_dict = {value.letter:value.code for (key, value) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input().upper()
phonetic_word_list = [nato_dict[letter]for letter in word]
print(phonetic_word_list)

