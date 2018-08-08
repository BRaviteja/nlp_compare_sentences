from nltk.corpus import wordnet as wn
from os.path import expanduser
home = expanduser("~")
from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
_path_to_model = home + '\\projects\\ml\\stanford-postagger\\models\\english-bidirectional-distsim.tagger'
_path_to_jar = home + '\\projects\\ml\\stanford-postagger\\stanford-postagger.jar'
st = POS_Tag(model_filename=_path_to_model, path_to_jar=_path_to_jar)

stop_words = set(stopwords.words('english'))
sentence1 = "I want to book a ticket "
tokens = word_tokenize(sentence1)
filtered_sentence = [w for w in tokens if not w in stop_words]

dict = {};
for token in filtered_sentence:
    synonyms = [];
    for syn in wn.synsets(token): 
        for l in syn.lemmas():
            synonyms.append(l.name())
        dict[token.lower()]= synonyms;
print(dict['book'])
print(len(dict))

sentence2 = 'I want to reserve a ticket'
tokens2 = word_tokenize(sentence2)

filtered_sentence_2 = [w for w in tokens2 if not w in stop_words]


sen1_pos_tag = st.tag(sentence1.split())
sen2_pos_tag = st.tag(sentence2.split())

word1_pos_tag = {}
word2_pos_tag = {}
for tag in sen1_pos_tag:
    word1_pos_tag[tag[0].lower()] = tag[1] 
for tag in sen2_pos_tag:
    word2_pos_tag[tag[0].lower()] = tag[1] 

print(word1_pos_tag)
print(word2_pos_tag)


for token in filtered_sentence:
    list = dict[token.lower()]
    if token not in filtered_sentence_2:
        for word in filtered_sentence_2:
            if word in list and word1_pos_tag[token.lower()] == word2_pos_tag[word.lower()]:
                print(token + ' in first sentence is synonym to ' + word + ' in 2nd sentence')