#!/usr/bin/python
#coding:utf8

import sys
import jieba
import codecs
import argparse

stopwords = set()
stopwords_path = "./stopwords.txt"

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("source_path",type=str)
	parser.add_argument("dest_path",type=str)
	args = parser.parse_args()
	return args

def load_stopwords():
	global args
	global stopwords
	with codecs.open(stopwords_path,"rb",encoding="utf-8") as file:
		for line in file:
			word = line.strip()
			if word:
				stopwords.add(word)
	

args = parse_args()
load_stopwords()
print(args)

corpus = codecs.open(args.source_path, "rb", encoding="utf-8")
dest = codecs.open(args.dest_path, "wb", encoding="utf-8")

# 分词，停用词处理
for line in corpus:
	words = jieba.lcut(line.strip())
	words = [ word for word in words if word.strip() and word not in stopwords ]
	text = "{}\n".format(" ".join(words))
	dest.write(text)

corpus.close()
dest.close()




