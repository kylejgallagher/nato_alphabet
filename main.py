import pandas as pd

nato = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index,row) in nato.iterrows()}

word = input("What's the word: ").upper()
phonetic = [nato_dict[letter] for letter in word]

print(phonetic)
