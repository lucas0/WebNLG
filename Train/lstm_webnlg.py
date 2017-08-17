import os
import cPickle as pickle
from gensim.models import word2vec
import gensim

cwd = os.getcwd()

unknown_token = "UNKNOWN_TOKEN"
sentence_end_token = "SENTENCE_END"

(triples,sentences, vocab) = pickle.load(open("save.p", "rb"))
print "LOADED X,Y data from pickle file: "+cwd+"/save.p"
model = gensim.models.Word2Vec.load(cwd+'/w2v_models/webnlg_corpus_model')
print "LOADED word2vec model from: "+cwd+"/w2v_models/webnlg_corpus_model\n"

print vocab[133][0]
f = model[vocab[133][0]]
print f
word=model.most_similar(positive=[f],topn=1)
print(word[0][0])