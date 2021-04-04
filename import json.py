import json

# Functions
def return_definition(thesaurus_dict: dict, word: str) -> str:
    """
    thesaurus_dict:     Dictionary containing words and their definition
    word:               Word you want to look up a definition for
    returns:            Definition of the word you provided
    """
    return thesaurus_dict[word]


with open("data.json") as file:
    data = json.load(file)

def_rain = return_definition(data, "rain")

print(def_rain)