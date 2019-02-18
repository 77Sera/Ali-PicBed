# coding:utf8

import time


def print_error(e, other_string=""):
    print("-----------ERROR------------\n")
    for line in other_string.split("|"):
        print(line)
    print(e)
    print("\n-----------E N D------------")


def get_time():
    '''
    # 将当前时间转换为 19-02-17的格式
    :return: tm[2:]  string => eg: 19-02-17
    '''
    tm = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    return tm[2:]


def get_timestamp_ram():
    '''
    截取时间戳的第4位后的6位数字，返回字符串形式
    :return: ts string
    '''
    ts = str(time.time())[4:10]
    return ts


def get_file_ext(file):
    '''
    获取文件后缀
    :return: ext string
    '''
    ext = ""

    file_name = file.split("/")[-1]
    temp = file_name.split(".")
    if len(temp) > 1:
        ext = "."+temp[-1]
    return ext


def load_config(config_file):
    '''
    :param config_file: string
    :return: r: dict
    '''
    r = {}
    with open(config_file,'r') as file:
        for line in file:
            line = line.replace("\n","")
            if len(line) and line[0] != "#":
                k,v = line.split("=")
                k,v = k.strip(),v.strip()
                r[k] = v
    return r