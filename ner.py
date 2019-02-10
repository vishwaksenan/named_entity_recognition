# importing spacy package 

import spacy

# this is the trickiest part. To load the english content, download the folder 'en_core_web_sm' or go to your spacy library folder and path the path.
# Additional installations may require  

nlp = spacy.load('en_core_web_sm/en_core_web_sm-2.0.0')

#initalizing the text to do Named Entity Recognition.
sample_text = nlp('Idhuke life-ah verrithuta , c the Indian politician , they arent the babies but oruthe stage padra , leave that PM   Aaven pakka pardesi (he loves travel) , here pplz are dying in  , he is attending  wedding mukiyama ?')

#printing the words and its related entity.
for word in sample_text.ents:
    print(word.text,word.label_)

# to get the the meaning of the label, we can use spacy.explain('<the_label>')

print(spacy.explain('NORP'))