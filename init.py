#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, dirname, abspath, isfile, isdir
import shutil

import helper as fn

dir_scr = dirname(abspath(__file__))
os.chdir(dir_scr)

def main():
    """
    initialize container
    """

    env_org = join(dir_scr, '_org', '.env')
    env_dst = join(dir_scr, '.env')
    if not isfile(env_dst):
        shutil.copyfile(env_org, env_dst)

    if not fn.input_yn("initialize container. ok? (y/*) :"):
        print("[info] initialize container canceled.")

    # .env読み込み
    param = fn.getenv(env_dst)

    # 環境変数を参照
    domain = param['DOMAIN']

    # コンテナ削除
    for line in fn.cmdlines(_cmd="docker-compose down"):
        sys.stdout.write(line)

    for line in fn.cmdlines(_cmd="docker-compose up -d"):
        sys.stdout.write(line)

    localhost = fn.local_ip()
    print(f"""\
----------gitlab started.

add hosts.
-----
{localhost} gitlab.{domain} mattermost.{domain} registry.{domain}
-----
""")

    print(f"""\
----------wait 5min to start gitlab
check status [docker-compose logs gitlab]

access to http://gitlab.{domain}/

and set root account password

""")

    print("----------container initialize end.")

# call main
if __name__ == "__main__":

    main()
