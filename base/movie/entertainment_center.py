# coding=utf-8
import logging
import re

import fresh_tomatoes
import get_movie
import media


def make_movies_list(info__list):
    """
    把返回的大列表拆分并重组成movie对象列表
    :param info__list: list[list,list....]
    :return: list[movie,movie...]
    """
    movies_list = []
    for info in info__list:
        # 如传入参数数量不对，屏幕打印错误信息并退出，返回值为错误1
        if info.__len__() != 4:
            logging.error("参数数量错误")
            exit(1)
        movies_list.append(media.Movie(info[0], info[1], info[2], remove_enter(info[3])))
    # 既然上面判断过个数了，这里应该可以放心使用0123角标，我本希望把list自动在参数位置转化为0123，不过没找到这种方法
    return movies_list


def remove_enter(storyline):
    """
    因为数据文件中有换行，所以最后一个元素后带了一个\n，这里使用正则去掉
    :param storyline: 
    :return: 
    """
    regex = re.compile('\n')
    return regex.sub('', storyline)


if __name__ == "__main__":
    # 以前的同事喜欢用这个来表示main函数，我也不知道这种写法出自哪里，但我自己也喜欢这么用
    # 已声明utf-8，所以应该可以用汉字注释？
    info_list = []
    fresh_tomatoes.open_movies_page(make_movies_list(get_movie.get_movie(info_list)))
