#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def hello():
    print 'hello world !'

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')

    hello()
