"""
사용예:
from actlib.file import file
file.getlineval(<파일>, <행번호>)
"""

import logging

logging.basicConfig(filename='log/err.log', format='%(asctime)s %(message)s', level=logging.INFO)


def getlineval(file, ln_no):
    """
    파일의 지정된 행에 값을 반환다.
    2020.08.23 actionshin@gmail.com
    :param file: 파일의 경로
    :param ln_no: 찾고자 하는 행번호
    :return: 문자열 행의 값
    """
    try:
        with open(file, 'r') as f:
            val = f.readlines()[ln_no - 1:ln_no][0]
            val = val.split('\n')[0]
            return val
    except (FileNotFoundError, IsADirectoryError) as err:
        logging.info("{}파일명이나 경로를 다시 확인하세요.".format(file))
        return
