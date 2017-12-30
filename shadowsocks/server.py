#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os.path
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))
from shadowsocks import utils


def main():
    utils.check_python()
    config = utils.get_config(False)


if __name__ == '__main__':
    main()
