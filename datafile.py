"""
판매 데이터가 있는 파일 객체
파일 정보를 가진다.
파일을 읽어 온다.
파일을 2차원 튜풀로 만들어 반환한다.
"""
import os
import logging
from actlib import fileext

file_list = []


class Sale:
    def __init__(self, file):
        self.file = file

    # 첫행에 작성된 지점명을 가져온다.
    def branch_name(self):
        return fileext.get_nth_line(self.file, 1)

    # 두번째 행에 작성된 판매자료를 가져온다.
    def sale_data(self):
        tmp = fileext.get_nth_line(self.file, 2)
        tmp = tmp.split(',')
        length = int(len(tmp)/2)
        return [(tmp[i], tmp[i+1]) for i in range(length)]

    # 과일가게 판매파일인지 확인
    def is_sale_data(self):
        result = True
        try:
            Sale.branch_name().index('_#fruitshop#_')
        except ValueError as err:
            logging.info('{}은 판매정보 파일이 아닙니다.'.format(self.file))
            return False
        return result


def make_monthly_data(target):
    for t in os.listdir(target):
        full_path = os.path.join(target, t)
        if os.path.isdir(full_path):
            make_monthly_data(full_path)
        else:
            file_list.append(full_path)
    # 월간 판매량을 구한다.
    # csv 형식으로 저장한다.


