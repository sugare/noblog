#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-2-25 上午7:20
# @Author  : Sugare
# @mail    : 30733705@qq.com
# @File    : memcache_mysql.py
# @Software: PyCharm

import memcache
import sys
from orm import noblog, tags

memc = memcache.Client(['127.0.0.1:11211'], debug=1)


def getData(bid):
    data = memc.get('b' + str(bid))

    if not data:
        try:
            data = noblog.get(noblog.id == bid)
        except:
            print('DoesNotExist the record')
            sys.exit(1)

        memc.set('b' + str(bid), data, 60*60*24*30)
        print('enter')

    return data

def delData(bid):
    if memc.get('b'+str(bid)):
        memc.delete('b'+str(bid))
    return True

def updateData(bid):
    delData(bid)
    getData(bid)



