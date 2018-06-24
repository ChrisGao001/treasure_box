#!/usr/bin/python

def parse_args():
	import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nr_bins', type=int, default=int(1e+6))
    parser.add_argument('-t', '--threshold', type=int, default=int(10))
    parser.add_argument('csv_path', type=str)
    parser.add_argument('gbdt_path', type=str)
    parser.add_argument('out_path', type=str)
    args = vars(parser.parse_args())
	return args

def hashstr(str, nr_bins):
	import hashlib
    return int(hashlib.md5(str.encode('utf8')).hexdigest(), 16)%(nr_bins-1)+1
