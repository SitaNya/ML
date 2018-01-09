import os.path
import re


def rename(strinfo):
    result = []
    dir = "/Users/sitanya/PycharmProjects/machine learning/base/rename/"
    list = os.listdir(dir)
    for str in list:
        old = dir + str
        new = dir + strinfo.sub('', str)
        print(old + " " + new)
        os.rename(old, new)

    return result


if __name__ == "__main__":
    strinfo = re.compile("\d")
    rename(strinfo)
