from pandas import read_csv


def phonetic_dict():
    data = read_csv('nato_phonetic_alphabet.csv')
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    return phonetic_dict


def phonetic_code(ph_dict):
    word = input("Enter a word: ").upper()
    try:
        output = [ph_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        phonetic_code(ph_dict)
    else:
        print(output)


phonetic_code(phonetic_dict())
