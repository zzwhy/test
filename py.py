#!/usr/bin/python
#!coding:utf-8

import time
import redis


Infervision = input("请输入限制时间的用户:")
if __name__ == "__main__":
    try:
        conn=redis.StrictRedis(host='127.0.0.1')
        conn.set('name',Infervision)
        conn.expire('name',100)   # 对用户进行时间限制
        for item in range(10):
            value=conn.get('name')
            if value != None:
                print(value.decode('utf8'))
            else:
                print('您输入的用户已过期')
                break
            time.sleep(2)
    except Exception as f:
        print(f)