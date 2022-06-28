import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os
import multiprocessing

#bind = "0.0.0.0:8000"   #绑定的ip与端口
bind = "127.0.0.1:8000" # 可自定义修改，其他地方可以不变，直接粘到你的项目中
backlog = 512                #监听队列数量，64-2048
#chdir = '/home/test/server/bin'  #gunicorn要切换到的目的工作目录
worker_class = 'sync' #使用gevent模式，还可以使用sync 模式，默认的是sync模式
workers = 4 # multiprocessing.cpu_count()    #进程数
threads = 16 #multiprocessing.cpu_count()*4 #指定每个进程开启的线程数
loglevel = 'info' #日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

# accesslog = "/home/log/gunicorn_access.log"      #访问日志文件
#errorlog = "/home/log/gunicorn_error.log"        #错误日志文件
accesslog = "-"  #访问日志文件，"-" 表示标准输出
errorlog = "-"   #错误日志文件，"-" 表示标准输出
proc_name = 'fof_api'   #进程名
