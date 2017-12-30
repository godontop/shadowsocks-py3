#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import getopt
import json
import logging
import os.path
import sys


def check_python():
    info = sys.version_info
    if info[0] == 2:
        print("Python 3.3+ required")
        sys.exit(1)
    elif info[0] == 3 and not info[1] >= 3:
        print("Python 3.3+ required")
        sys.exit(1)
    elif info[0] not in [2, 3]:
        print("Python version not supported")
        sys.exit(1)


def find_config():
    config_path = 'config.json'
    if os.path.exists(config_path):
        return config_path
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.json')
    if os.path.exists(config_path):
        return config_path
    return None


def get_config(is_local):
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(message)s')

    if is_local:
        shortopts = 'hd:s:b:p:k:l:m:c:t:vq'
        longopts = ['help', 'fast-open', 'pid-file=', 'log-file=']
    else:
        shortopts = 'hd:s:p:k:m:c:t:vq'
        longopts = ['help', 'fast-open', 'pid-file=', 'log-file=', 'workers=']
    try:
        config_path = find_config()
        optlist, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
        for key, value in optlist:
            if key == '-c':
                config_path = value

        if config_path:
            logging.info('loading config from %s' % config_path)
            with open(config_path, 'rb') as f:
                try:
                    config = json.loads(f.read().decode('utf-8'),
                                        object_hook=_decode_dict)
                except Exception as e:
                    raise e
    except Exception as e:
        raise e
