import argparse
'''
refer to https://www.jianshu.com/p/fef2d215b91d
'''

parser = argparse.ArgumentParser()
# given default value
parser.add_argument("-n","--threads",type=int, default=5,help="the number of the thread")
# default is bool 
parser.add_argument("-q","--quiet",action="store_true")
parser.add_argument("-d", "--damen", type=int, default=0, choices=[1,0])

# position parameter
parser.add_argument("src_path",type=str)
args = parser.parse_args()
print(args.src_path)
print(args.threads)
print(args)
