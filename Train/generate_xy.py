import itertools
import os
import unicodedata
from bs4 import BeautifulSoup as bs
import cPickle as pickle
import nltk
from gensim.models import word2vec
import gensim

cwd = os.getcwd()

INPUT_FILE = "ALL.xml"

X =[]
Y =[]

# PART 1
# this part only reads the XML and creates the 
# X list (of mtriples) and the Y list (of sentences) by crossproduct
with open(INPUT_FILE, "r+") as f:
	soup = bs(f, "lxml")
	# entry = entry
	# mtriple = triples
	# lex = sentence
	for elem in soup.findAll('entry'):
		elem_id = elem.get('eid')
		triples = [e.string.encode('ascii', 'ignore') for e in elem.findAll('mtriple')]
		sentences = [e.string.encode('ascii', 'ignore') for e in elem.findAll('lex')]

		# print elem_id,triples
		# print "======"
		# print sentences
		for e in list(itertools.product(triples,sentences)):
			X.append(e[0])
			Y.append(e[1])
		# with open(cwd+"/extracted_sentences/"+domain+".txt","a+") as output:
		# 	sentence = elem.string.encode('utf-8')
		# 	output.write(sentence+'\n')

# PART 2
# now we define the vocabulary size, 
# and create the w2v representations for each word in the vocabulary
vocabulary_size = 80000
unknown_token = "UNKNOWN_TOKEN"
sentence_end_token = "SENTENCE_END"

# # Read the data and append SENTENCE_END tokens
# # Append SENTENCE_END
# triples = ["%s %s" % (x, sentence_end_token) for x in X]
# sentences = ["%s %s" % (y, sentence_end_token) for y in Y]
# # print "Parsed %d sentences." % (len(sentences))
# # >> Parsed 53786 sentences.

# # Tokenize the sentences into words
# # tokenized_triples = [nltk.word_tokenize(sent) for sent in triples]
# tokenized_sentences = [nltk.word_tokenize(sent) for sent in sentences]
 
# # Count the word frequencies
# word_freq = nltk.FreqDist(itertools.chain(*tokenized_sentences))
# # print "Found %d unique words tokens." % len(word_freq.items())
# # >> Found 5921 unique words tokens.
# vocabulary_size = len(word_freq.items())
# vocab = word_freq.most_common(vocabulary_size-1)

# # SAVE DATA INTO PICKLE
# # X is triples
# # Y is sentences
# pickle.dump((triples,sentences, vocab), open("save.p", "wb"))
# print "SAVED X,Y data into pickle file: "+cwd+"/save.p"
(triples,sentences, vocab) = pickle.load(open("save.p", "rb"))
print "LOADED X,Y data from pickle file: "+cwd+"/save.p"

# print "The most frequent word in our vocabulary is '%s' and appeared %d times." % (vocab[0][0], vocab[0][1])
# print "The least frequent word in our vocabulary is '%s' and appeared %d times." % (vocab[-1][0], vocab[-1][1])

# # train word2vec on the two sentences
# model = word2vec.Word2Vec(tokenized_sentences, min_count=1)

# # SAVE W2V MODEL
# model.save(cwd+'/w2v_models/webnlg_corpus_model')
# print "SAVED word2vec model into: "+cwd+"/w2v_models/webnlg_corpus_model\n"
model = gensim.models.Word2Vec.load(cwd+'/w2v_models/webnlg_corpus_model')
print "LOADED word2vec model from: "+cwd+"/w2v_models/webnlg_corpus_model\n"

print vocab[:5]
f = model[vocab[123][0]]
print f
word=model.most_similar(positive=[f],topn=1)
print(word[0][0])

# index_to_word.append(unknown_token)
# word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])
 
# print "Using vocabulary size %d." % vocabulary_size
# print "The least frequent word in our vocabulary is '%s' and appeared %d times." % (vocab[-1][0], vocab[-1][1])
 
# # Replace all words not in our vocabulary with the unknown token
# for i, sent in enumerate(tokenized_sentences):
#     tokenized_sentences[i] = [w if w in word_to_index else unknown_token for w in sent]
 
# print "\nExample sentence: '%s'" % sentences[0]
# print "\nExample sentence after Pre-processing: '%s'" % tokenized_sentences[0]
 
# # Create the training data
# X_train = np.asarray([[word_to_index[w] for w in sent[:-1]] for sent in tokenized_sentences])
# y_train = np.asarray([[word_to_index[w] for w in sent[1:]] for sent in tokenized_sentences])

# pickle.dump((X_train,y_train,index_to_word,word_to_index), open("save.p", "wb"))


