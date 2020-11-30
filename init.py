#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, dirname, abspath, isfile, isdir

dir_scr = dirname(abspath(__file__))
import helper as fn

def main():
    """
    initialize container
    """
    # .env読み込み
    param = fn.getenv(".env")

    # 環境変数を参照
    container = param['CONTAINER_NAME']
    domain = param['DOMAIN']

    os.chdir(dir_scr)
    dir_vol = join(dir_scr, 'vol')

    # reset volumes
    fn.rmdir(dir_vol)
    if not isdir(dir_vol):
        os.makedirs(dir_vol)
    os.chmod(dir_vol, 0o777)

    # コンテナ削除
    cmds = [
        "docker-compose down",
        "docker-compose up -d",
    ]
    for line in fn.cmdlines(_cmd="docker-compose down"):
        sys.stdout.write(line)

    for line in fn.cmdlines(_cmd="docker-compose up -d"):
        sys.stdout.write(line)

    localhost = fn.local_ip()
    print(f"""\
----------gitlab started.

add to hosts.
-----
{localhost} gitlab.{domain} mattermost.{domain} registry.{domain}
-----

----------wait 5min to start gitlab
check status [docker-compose logs gitlab]

access to http://gitlab.{domain}/

and set root account password

""")

    print("----------container initialize end.")

# call main
if __name__ == "__main__":

    if fn.input_yn("initialize container. ok? (y/*) :"):
        main()
    else:
        print("[info] initialize container canceled.")
