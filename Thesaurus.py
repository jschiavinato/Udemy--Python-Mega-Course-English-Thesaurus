# Import json module
import json

# Import Spellchecker
from spellchecker import SpellChecker

spell = SpellChecker()

# Load json file
data = json.load(open("data.json"))

#aswk the word
word = input('Which word do you want to know? ')


#  Function to search for the word
def translate(word):
    if word in data:
        for item in data[word]:
            print(item)
    else:
        c = spell.correction(word)
        if c.title() in data: #check if the word corrected is a country or a city 
            for item in data[word.title()]:
                print(item)
        elif c.upper() in data: #check if the word is an acronym
            for item in data[c.upper()]:
                print(item)
        else:
            i = 1
            while i > 0:
                confirm = input('Did you mean' +" "+ c + '?' + " " + "[Yes/No]").lower()
                if confirm in ['yes','y']:
                    if c in data:
                        for item in data[c]:
                            print(item)
                            i = 0
                    else:    
                        print('This word was not found in our database')
                        i = 0
                elif confirm in ['no','n']:
                    print('We did not understand your query')
                    i = 0 
                else:
                    continue
    
     
#run the function 
if word.lower() in data:
    translate(word.lower())
else:
    translate(word)

