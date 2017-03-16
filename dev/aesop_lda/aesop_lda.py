import json
import logging
import gensim

def clean_list(txt):
    stoplist = set('for a of the and to in or by not as so this that'.split())
    return [w for w in txt.split() if w not in stoplist]

def alloc(n,lda):
    x = [0]*n
    for t in lda:
        x[t[0]] = t[1]
    return x

if __name__=="__main__":
#    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
#                        level=logging.INFO, filename='lda.log',)

    with open("/home/ubuntu/data/read_gov_aesop/all.txt",'r') as f:
        ndocs = f.read().split("\n")
        ndocs = [ d.split("#") for d in ndocs if len(d.strip())>0 ]
        docs  = [ d[1] for d in ndocs ]
        nd    = [ d[0] for d in ndocs ]

    texts = [clean_list(d) for d in docs]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(t) for t in texts]
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, \
                                          id2word=dictionary,\
       num_topics=10, update_every=1, chunksize=10000, passes=100)

#    with open('texts_corpus.json','w') as f:
#         json.dump({"texts":texts,"corpus":corpus},f)
#    dictionary.save('dictionary.gensim')
#    lda.save('lda10.gensim')
#    lda.print_topics(10)
    r = [ alloc(10,lda[t]) for t in corpus ]
    res = { d[0]:d[1] for d in zip(nd,r)}
    
    with open('aesop_lda.json','w') as f:
        json.dump(res,f) 
