"""
판매 데이터가 있는 파일 객체
파일 정보를 가진다.
파일을 읽어 온다.
파일을 2차원 튜풀로 만들어 반환한다.
"""
import os
import logging
from actlib import fileext

# get_target_files()를 통해 디렉토리의 파일목록을 가져온다.
file_list = []


class Sale:
    def __init__(self, file):
        self._file = file

    @property
    def file_name(self):
        return self._file

    # 첫행에 작성된 지점명을 가져온다.
    @property
    def branch_name(self):
        return fileext.get_nth_line(self._file, 1)

    # 두번째 행에 작성된 판매자료를 가져온다.
    @property
    def sale_data(self):
        tmp = fileext.get_nth_line(self._file, 2)
        tmp = tmp.split(',')
        length = int(len(tmp) / 2)
        return [(tmp[i], tmp[i + 1]) for i in range(length)]


# 판매정보 파일인지 확인
def is_sale_data(obj):
    result = True
    try:
        obj.branch_name.index('_#fruitshop#_')
    except ValueError as err:
        logging.info('{}은 판매정보 파일이 아닙니다.'.format(obj.file_name))
        return False
    return result


# 지정된 월의 판매정보 파일 목록을 가져온다.
def get_target_files(target):
    for t in os.listdir(target):
        full_path = os.path.join(target, t)
        if os.path.isdir(full_path):
            get_target_files(full_path)
        else:
            # 판매정보인 경우만 목록에 추가
            if is_sale_data(Sale(full_path)):
                file_list.append(full_path)
    return file_list


# 월간 판매량을 구한다.
def get_monthly_sale_data():
    pass


# csv 형식으로 저장한다.
def sale_data_to_csv():
    pass


if __name__ == "__main__":
    """
    모듈 테스트
    """
    target = os.path.join(os.getcwd(), 'sample', '202007')
    # 모듈 사용시 클로저
    get_target_files(target)
