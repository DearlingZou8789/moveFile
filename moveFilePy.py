#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,time, shutil

def parseFile(f, targetDirectory):
    if  os.path.isfile(f):
        statInfo = os.stat(f)
        localTime = time.localtime(statInfo.st_mtime)
        print(localTime)
        fileExt = os.path.split(f)
        directory = targetDirectory + str(localTime[0]) + '/' + ("%.2d" % localTime[1]) + '/' + ("%.2d" % localTime[2])
        if not os.path.isdir(directory):
            os.makedirs(directory)
        targetFile = directory + '/' + fileExt[1];
        print(targetFile)
        shutil.move(f, targetFile)

def parseDirectory(directory, targetDirectory = './'):
    if not os.path.exists(targetDirectory) :
        os.makedirs(targetDirectory)
    start = time.time()
    num = 0
    if os.path.isdir(directory):
        for x in os.listdir(directory):
            file = directory + '/' + x
            parseFile(file, targetDirectory)
            num += 1
    end = time.time()
    print('总共花费%d时间，%d张图片' % ((end - start), num))

if  __name__ == '__main__':
    file = './image'
    parseDirectory(file)
