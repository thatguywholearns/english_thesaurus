import json
from difflib import get_close_matches

# Functions
def return_definition(thesaurus_dict: dict, word: str) -> list:
    """
    thesaurus_dict:     Dictionary containing words and their definition
    word:               Word you want to look up a definition for
    returns:            List that contains definition(s) of the word you provided
    """
    # Clean input
    word_clean = word.strip().lower()
    if word_clean in thesaurus_dict:
        return thesaurus_dict[word_clean]
    if word_clean.title() in thesaurus_dict:
        return thesaurus_dict[word_clean.title()]
    elif len(get_close_matches(word=word_clean, possibilities=thesaurus_dict, cutoff=0.5)) > 0:
        closest_word = get_close_matches(word=word_clean, possibilities=thesaurus_dict, cutoff=0.5)[0]
        print(f"Did you mean {closest_word}")
        user_feedback = input("[Y/N]\n")
        if user_feedback == "Y":
            return thesaurus_dict[closest_word]
        elif user_feedback == "N":
            return "The word doesn't exist"
        else:
            "Can't recognize input"
    else:
        return "Definition not found"


# Start app
with open("data.json") as file:
    data = json.load(file)

user_input = str(input("Enter a word: "))

def_word = return_definition(data, user_input)

print(def_word)