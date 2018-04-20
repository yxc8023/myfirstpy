# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'https://blog.csdn.net/gates0087/article/details/79422694'
    req = requests.get(target)
    print(req.text)