#!usr/bin/python
# -*- coding: utf-8 -*-
import time
while True:
    try:
        date=input('请输入日期：')
        struct_time=time.strptime(date,'%Y-%m-%d')
    except ValueError as e:
        print("输入日期有误:{e}\n请重新输入".format(e=e))
        continue
    else:
        print(struct_time.tm_yday)
        break