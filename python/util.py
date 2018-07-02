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

import logging
def init_log(file_name,logger_name=None,level=logging.INFO):
    logger = logging.getLogger(logger_name)
    handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=10*1024*1024, backupCount=5)
    if logger_name is None:
        handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(message)s", "%Y-%m-%d %H:%M:%S"))
    else:
        handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s <%(module)s> %(message)s", "%Y-%m-%d %H:%M:%S"))
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
# log.debug log.info log.error()

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s] %(levelname)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
import hashlib
def md5(str):
    
    m = hashlib.md5()
    m.update(str)
    psw = m.hexdigest()
    return psw
    
import urllib2
def request(url):
    req = urllib2.Request(url=url)
    res = urllib2.urlopen(req)
    data = res.read()
    return data

import os
def disk_free_usage(path):  
    """Return disk usage associated with path."""  
    st = os.statvfs(path)  
    free = (st.f_bavail * st.f_frsize)  
    total = (st.f_blocks * st.f_frsize)  
    used = (st.f_blocks - st.f_bfree) * st.f_frsize  
    try:  
        percent = ret = (float(used) / total) * 100  
    except ZeroDivisionError:  
        percent = 0  
    # NB: the percentage is -5% than what shown by df due to  
    # reserved blocks that we are currently not considering:  
    # http://goo.gl/sWGbH  
    return free
    
    
################################ Download ##################################

from time import sleep
import urllib

class RateLimit(object):
    """Rate limit a url fetch"""
    def __init__(self, rate_limit):
        """rate limit in kBytes / second"""
        self.rate_limit = rate_limit
        self.start = time()

    def __call__(self, block_count, block_size, total_size):
        total_kb = total_size / 1024
        downloaded_kb = (block_count * block_size) / 1024
        elapsed_time = time() - self.start
        if elapsed_time != 0:
            rate = downloaded_kb / elapsed_time
            #print "%d kb of %d kb downloaded %f.1 kBytes/s\n" % (downloaded_kb ,total_kb, rate),
            expected_time = downloaded_kb / self.rate_limit
            sleep_time = expected_time - elapsed_time
            #print "Sleep for", sleep_time
            if sleep_time > 0:
                sleep(sleep_time)
                
def download(url, dest):
    try:
        urllib.urlretrieve(url,dest,reporthook=RateLimit(RATE_LIMIT))
        return True
    except Exception,e:
        print e
        return False     
######################## End of Download ##################################
import commands
def shell_cmd(cmd):
    try:
        s, o = commands.getstatusoutput(cmd)
    except Exception,e:
        print e
        return None
    return (s,o)

###############################  time ##############################################
import datetime
def get_day(offset=0):
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=offset)
    day = now + delta;
    return day.strftime('%Y-%m-%d')
	
def get_script_path():
	return os.path.dirname(os.path.realpath(__file__))

import os
def make_dirs(dirs):
	return os.makedirs(dirs)

            
