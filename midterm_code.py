

import spacy #package

words = spacy.load("en_core_web_sm") #the directory (which is referred to multiple times)

user_input = input("Type your sentence : ")

phrase = words(user_input) #compares the user input to information in directory

#uses an if statement to check if phrase matches token in the directory to see if verb
print("\nThe verbs are :", [token.lemma_ for token in phrase if token.pos_ == "VERB"]) 
    

print("\nThe Nouns are :", [chunk.text for chunk in phrase.noun_chunks], "\n") # for loop that traveses through the text, printing out the nouns


#matches what is in the phrase to what they are technically
text_example = [
    "As of October 2022, Bill Gates had an estimated net worth of US$107 billion, making him the fifth-richest person in the world.", 
    "Later in his career and since leaving day-to-day operations at Microsoft in 2008, Bill Gates has pursued many business and philanthropic endeavors."
]

#takes the directory into a document disabling certain fearures 
for doc in words.pipe(text_example, disable=["tok2vec", "tagger", "parser", "attribute_ruler", "lemmatizer"]):
    
    #takes what is in the text, and labels what that part of the text is. 
    print([(ent.text, ent.label_) for ent in doc.ents])


