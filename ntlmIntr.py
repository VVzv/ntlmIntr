# !/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import os
import time
import argparse
import threading

from passlib.hash import nthash


def ntmlInt(passwd, hash_passwd, semaphore, info):
    semaphore.acquire()
    try:
        if info:
            print("\033[36m[{}] {}:{}\033[0m".format(time.strftime('%H:%M:%S', time.localtime()), hash_passwd, passwd))
        ver = nthash.verify(passwd, hash_passwd)
        if ver:
            print("\033[1;32m[+] Find: {}['{}']\033[0m".format(hash_passwd, passwd))
            os.system("kill -9 {}".format(os.getpid()))
    except:
        pass
    semaphore.release()

if __name__ == '__main__':
    use = '''\033[35m
  python3 ntmlIntr.py -p 32ed87bdb5fdc5e9cba88547376818d4 -f password.txt
  python3 ntmlIntr.py -p 32ed87bdb5fdc5e9cba88547376818d4 -f password.txt -t 50
  python3 ntmlIntr.py -p 32ed87bdb5fdc5e9cba88547376818d4 -f password.txt -t 50 -v'''
    parse = argparse.ArgumentParser(usage=use)
    parse.add_argument('-p', '--ntml', type=str, help='NTML密文')
    parse.add_argument('-f', '--file', type=argparse.FileType('r'), help='本地明文密码字典')
    parse.add_argument('-t', '--thread', type=str, default=30)
    parse.add_argument('-v', '--verbosity', action="store_true", help='显示爆破记录')
    args = parse.parse_args()
    if args.ntml is None and args.file is None:
        parse.print_help()
    try:
        start_time = time.time()
        semaphore = threading.BoundedSemaphore(args.thread)
        hash_pass = args.ntml
        pass_list = args.file.readlines()
        for passwd in pass_list:
            if args.verbosity:
                t = threading.Thread(target=ntmlInt, args=(passwd.strip(), hash_pass, semaphore, True))
                t.start()
            else:
                t = threading.Thread(target=ntmlInt, args=(passwd.strip(), hash_pass, semaphore, False))
                t.start()
        while threading.active_count() != 1:
            pass
        print("\033[36m[>>>] 执行完成!\033[0m")
    except:
        pass

