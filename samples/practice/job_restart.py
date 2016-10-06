#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/10/6 20:31
# @Author  : Hercwey
# @Site    : 
# @File    : job_restart.py
# @Software: PyCharm

####################################################################
# python 自动重启本程序
####################################################################
# import os,time
# def close():
#  print "程序重启！！！！"
#  print time.strftime('%Y.%m.%d-%H.%M.%S')
#  time.sleep(2) #3秒
#  p = os.popen('11111111.bat')
#  while True:
#    line = p.readline();
#    if '' == line:
#      break
#    print line
# if __name__ == '__main__':
#  close()
####################################################################
"""
每小时重启一下百度云管家
"""
import os
import time

YUNGUANJIA_EXE = r'C:\Users\Administrator.HXICBAVUV7DWEV6\AppData\Roaming\Baidu\BaiduYunGuanjia\baiduyunguanjia.exe'


def restart_program():
    os.system('taskkill /f /im baiduyunguanjia.exe')
    time.sleep(10)
    os.system(YUNGUANJIA_EXE)


if __name__ == "__main__":
    while True:
        print "Restarting..."
        restart_program()
        print "Restarted"
        print "Yunguanjia will be restarted in a hour later"
        time.sleep(3600)
