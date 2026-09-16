import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
pd_df = pandas.read_csv("./Day26-List-Comprehension-and-the-Nato-Alphabet/nato_phonetic_alphabet.csv")

pd_dict = {row.letter:row.code for (index, row) in pd_df.iterrows()}
# print(pd_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
word_dict = [pd_dict[letter] for letter in user_input]
print(word_dict)
    