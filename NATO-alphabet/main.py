import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Please provide a word: ").upper()

result = [data_dict[letter] for letter in user_word]

print(result)

