#!/usr/bin/python
#!coding:utf-8

import time
import redis


tmp = input("请输入用户名:")
if __name__ == "__main__":
    try:
        conn=redis.StrictRedis(host='127.0.0.1')
        conn.set('name',tmp)
        conn.expire('name',10)   # 设置过期时间
        for item in range(12):
            value=conn.get('name')
            if value != None:
                print(value.decode('utf8'))
            else:
                print('access denied.....')
                break
            time.sleep(2)
    except Exception as f:
        print(f)