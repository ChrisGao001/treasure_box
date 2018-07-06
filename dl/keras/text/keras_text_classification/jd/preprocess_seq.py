#!/usr/bin/python
#coding:utf8

import sys
import codecs
import argparse
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("source_path",type=str)
	args = parser.parse_args()
	return args

args = parse_args()
print(args)

source = codecs.open(args.source_path, "rb", encoding="utf-8")
x_text = source.readlines()
y = [ 1 for _ in range(len(x_text)) ]

# 参数num_words,filters,lower,split
tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',lower=True,split=" ")
tokenizer.fit_on_texts(x_text)
vocab = tokenizer.word_index
idx2word = tokenizer.index_word
x_train, x_test, y_train, y_test = train_test_split(x_text, y, test_size=0.2, random_state=2017)

x_train_word_ids = tokenizer.texts_to_sequences(x_train)
x_train_padded_seqs = pad_sequences(x_train_word_ids, maxlen=64)
# 提取特征词袋模式"binary", "count", "tfidf", "freq".
x_train = tokenizer.sequences_to_matrix(x_train_word_ids, mode='binary')
	

