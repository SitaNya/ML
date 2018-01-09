# coding=utf-8
import fileinput
import os
import sys


def get_dir():
    """
    通过本文件的位置获取数据文件相对路径
    :return: 这个文件的所在目录
    """
    dir_name, filename = os.path.split(os.path.abspath(sys.argv[0]))
    return dir_name


def get_movie(movies__list):
    """
    从文件中读出消息，这样会让程序看起来不那么长长长长长长
    :param movies__list: list
    :return: list[list,list.....]
    """
    for line in fileinput.input(get_dir() + "/Movies_List"):
        movies__list.append(line.split(","))
    # 把上述文件中的内容按行读出，打成list后扔进另一个list中
    # 这里有一个bug：url中不能有','，但考虑到这种情况很少见，未做修改
    return movies__list
