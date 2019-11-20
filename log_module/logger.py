# -*- coding: utf-8 -*-
import logging
import os
import sys
from PIL import ImageGrab
import time


class logger:
    def __init__(self, set_level="",
                 name=os.path.split(os.path.splitext(sys.argv[0])[0])[-1],
                 # log_name=time.strftime("%Y-%m-%d.log", time.localtime()),
                 log_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "log"),
                 use_console=True,
                 shot=False,):
        status=True

        # nameCode转化为名字
        #if name=='':
        #    pass

        log_name=name+time.strftime("_%Y-%m-%d.log", time.localtime())+'.log'
        self.logger = logging.getLogger(name)

        if set_level.lower() == "critical":
            self.logger.setLevel(logging.CRITICAL)
        elif set_level.lower() == "error":
            self.logger.setLevel(logging.ERROR)
        elif set_level.lower() == "warning":
            self.logger.setLevel(logging.WARNING)
        elif set_level.lower() == "info":
            self.logger.setLevel(logging.INFO)
        elif set_level.lower() == "debug":
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.NOTSET)

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        log_file_path = os.path.join(log_path, log_name)
        log_handler = logging.FileHandler(log_file_path,encoding='utf-8')
        mark='?'
        log_handler.setFormatter(logging.Formatter("[%(asctime)s] {} %(name)s {} [%(levelname)s] {} %(message)s".format(mark,mark,mark)))
        self.logger.addHandler(log_handler)
        if use_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter("[%(asctime)s] - %(name)s - [%(levelname)s] - %(message)s"))
            self.logger.addHandler(console_handler)



    def screenshot(self,screenshot=False):
        if screenshot==True:
            screenshot = ImageGrab.grab()
            snap_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     'image\\' + self.logger.name + time.strftime('_%Y-%m-%d_%H-%M-%S_.jpg',time.localtime()))
            screenshot.save(snap_path)

    def addHandler(self, hdlr):
        self.logger.addHandler(hdlr)

    def removeHandler(self, hdlr):
        self.logger.removeHandler(hdlr)

    def critical(self, msg, *args, **kwargs):
        if logger(shot=True):
            self.screenshot(screenshot=True)
        self.logger.critical(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        if logger(shot=True):
            self.screenshot(screenshot=True)
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        if logger(shot=True):
            self.screenshot(screenshot=True)
        self.logger.error(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        # if logger(shot=True):
        #     self.screenshot(screenshot=True)
        self.logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        # if logger(shot=True):
        #     self.screenshot(screenshot=True)
        self.logger.debug(msg, *args, **kwargs)

    def log(self, level, msg,  *args, **kwargs):
        self.logger.log(level, msg, *args, **kwargs)

mylog = logger(name='test',set_level='',shot=False)
mylog.warning('125125251')
mylog.log(30,'sadasfaf')
mylog.screenshot(True)
mylog.log(50,'cnm')
mylog.log(3,'w114')
print(123124251)
mylog.debug('1231313')