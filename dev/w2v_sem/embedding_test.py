from gensim.models.keyedvectors import KeyedVectors
import sys

wv = KeyedVectors.load_word2vec_format(sys.argv[1], binary=False)

print wv.most_similar(positive=['woman', 'king'], negative=['man'])

#print wv.similarity('woman', 'man')

#print wv.evaluate_word_pairs("tests/wordsim353.low.tsv")

acc = wv.accuracy("tests/google_questions_words.low.txt",restrict_vocab=50000)
for a in acc: print a["section"], len(a["correct"]), len(a["incorrect"])

with open("tests/google_questions_words.low.txt","r") as f:
    questions = f.read().split("\n")

acc = {}
current_section = ""
for q in questions:
    q = q.strip()
    if len(q) == 0: continue
    if q[0] == ":":
        acc[q] = [0]*10
        current_section = q
        continue
    w = q.split()
    if w[0] not in wv or w[1] not in wv or \
       w[2] not in wv or w[3] not in wv:
        continue
    sim = wv.most_similar(positive=[w[1],w[2]], negative=[w[0]])
    counter = 0
    for s in sim:
        if s[0] == w[3] and counter < 10:
            acc[current_section][counter] += 1
            break
        counter += 1

tot4 = 0
for a in acc:
    tot4 += sum(acc[a][:4])
    print a, sum(acc[a])
    print acc[a]    

print tot4

