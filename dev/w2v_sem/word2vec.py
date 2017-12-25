import numpy as np
import sys
import random
import tensorflow as tf
import json
import math


def generate_batch(pairs,index,batch_size,epoch):
    batch  = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    do_shuffle = False
    for i in range(batch_size):
        batch[i]  = pairs[index][0]
        labels[i] = pairs[index][1]
        index += 1
        if index >= len(pairs):
            index = 0
            do_shuffle = True
            epoch += 1
    return batch, labels, index, epoch, do_shuffle



if __name__=="__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    with open(infile,"r") as f:
        pairs = json.load(f)

    with open("words.json","r") as f:
        voc = json.load(f)
        voc = voc["voc"]

    # parameters
    batch_size = 64 
    embedding_size = 300
    voc_size = len(voc)
    num_sampled = 65 
    # definitions
    graph = tf.Graph()
    with graph.as_default(), tf.device('/cpu:0'):
        train_dataset = tf.placeholder(tf.int32, shape=[batch_size])
        train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
        embeddings = tf.Variable(
            tf.random_uniform([voc_size, embedding_size], -1.0, 1.0))
        softmax_weights = tf.Variable(
            tf.truncated_normal([voc_size, embedding_size],
            stddev=1.0 / math.sqrt(embedding_size)))
        softmax_biases = tf.Variable(tf.zeros([voc_size]))
        embed = tf.nn.embedding_lookup(embeddings, train_dataset)
        loss = tf.reduce_mean(
            tf.nn.sampled_softmax_loss(
                weights=softmax_weights,
                biases=softmax_biases, 
                inputs=embed,
                labels=train_labels, 
                num_sampled=num_sampled, 
                num_classes=voc_size))
        optimizer = tf.train.AdagradOptimizer(1.0).minimize(loss)
        norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, 
            keep_dims=True))
        normalized_embeddings = embeddings / norm

    index = 0
    epoch = 0    

    num_steps = 100000000
    with tf.Session(graph=graph) as session:
        tf.global_variables_initializer().run()
        total_loss = 0
        for step in range(num_steps):
            batch, labels, index, epoch, do_shuffle =\
                 generate_batch(pairs,index,batch_size,epoch)
            #if do_shuffle: random.shuffle(pairs)
            feed_dict = {train_dataset:batch, train_labels:labels}
            _, l = session.run([optimizer, loss], feed_dict=feed_dict)
            total_loss += l
            if step % 1000 == 0 and step>0:
                print('loss %d %d: %f %f' % (epoch,step,total_loss,l))
            if step % 1000000 == 0 and step>0:
                embeddings = normalized_embeddings.eval()
                with open(outfile,"w") as f: 
                    json.dump(embeddings.tolist(),f)
        embeddings = normalized_embeddings.eval()
        
    with open(outfile,"w") as f: json.dump(embeddings.tolist(),f)


