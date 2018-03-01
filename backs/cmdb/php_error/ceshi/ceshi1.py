#coding=utf-8
import  json
import yaml
filename = "php_error.log"

for i in open(filename):
    if i == "\n":
        pass
    else:
        print i
