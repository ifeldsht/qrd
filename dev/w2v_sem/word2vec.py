# SRO2vec - generates SRO embeding vectors 
# Takes files like sro2vec_input10.json, outputs sro2vec_embed10.json

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
    with open(sys.argv[1],"r") as f:
        data = json.load(f)
    pairs = data["pairs"]

    # parameters
    batch_size = 128
    embedding_size = 32
    voc_size = len(data["dict"])
    num_sampled = 64
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
            tf.nn.sampled_softmax_loss(softmax_weights, softmax_biases, 
            embed,train_labels, num_sampled, voc_size))
        optimizer = tf.train.AdagradOptimizer(1.0).minimize(loss)
        norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, 
            keep_dims=True))
        normalized_embeddings = embeddings / norm

    index = 0
    epoch = 0    

    num_steps = 1000000
    with tf.Session(graph=graph) as session:
        tf.global_variables_initializer().run()
        average_loss = 0
        for step in range(num_steps):
            batch, labels, index, epoch, do_shuffle =\
                 generate_batch(pairs,index,batch_size,epoch)
            if do_shuffle: random.shuffle(pairs)
            feed_dict = {train_dataset:batch, train_labels:labels}
            _, l = session.run([optimizer, loss], feed_dict=feed_dict)
            average_loss += l
            if step % 2000 == 0 and step>0:
                average_loss = average_loss / 2000
                print('loss %d %d: %f' % (epoch,step, average_loss))
                average_loss = 0
        embeddings = normalized_embeddings.eval()

    data["embeddings"] = embeddings.tolist()

    with open(sys.argv[2],"w") as f:
        json.dump(data,f)


