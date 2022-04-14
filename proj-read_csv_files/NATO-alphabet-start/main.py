import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in file.iterrows()}

name = input("Enter your name?")
name_ac = [item for item in name]
name_ac = [name.upper() for name in name_ac]
list1 = [new_dict[item] for item in name_ac ]


print(list1)