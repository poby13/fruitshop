"""
판매 데이터가 있는 파일 객체
파일 정보를 가진다.
파일을 읽어 온다.
파일을 2차원 튜풀로 만들어 반환한다.
"""
import os
import logging
from actionlib import fileext
from pathlib import Path

_file_list = []
_sale_data = {}


class Sale:
    def __init__(self, file):
        # __는 클래스 속성명을 맹글링하여 클래스간 속성명 충돌을 방지한다.
        self.__file = file

    @property
    def file_name(self):
        return self.__file

    # 첫행에 작성된 지점명을 가져온다.
    @property
    def branch_name(self):
        return fileext.get_nth_line(self.__file, 1)

    # 두번째 행에 작성된 판매자료를 가져온다.
    @property
    def sale_data(self):
        temp = fileext.get_nth_line(self.__file, 2)
        temp = temp.split(',')
        length = int(len(temp) / 2)
        return [(temp[_ * 2], int(temp[_ * 2 + 1])) for _ in range(length)]


# 판매정보 파일인지 확인
# object_는 예약어와 겹치는 문제를 피하기 위해 _를 붙인다.
def is_sale_data(object_):
    temp = True
    try:
        object_.branch_name.index('_#fruitshop#_')
    except ValueError as err:
        logging.info('{}은 판매정보 파일이 아닙니다.'.format(object_.file_name))
        return False
    return temp


# 지정된 월의 판매정보 파일 목록을 재귀적으로 처리하여 가져온다.
def get_dir_files(target):
    for _ in os.listdir(target):
        path = os.path.join(target, _)
        if os.path.isdir(path):
            get_dir_files(path)
        else:
            # 판매정보인 경우만 목록에 추가
            if is_sale_data(Sale(path)):
                _file_list.append(path)
    return _file_list


# 월간 판매량을 구한다.
def get_monthly_sale_data(file):
    obj = Sale(file)
    # 판매자료가 아닌 경우 걸러낸다.
    if not is_sale_data(obj):
        print(f'{file}은 판매자료가 아닙니다.')
        del obj
        return False
    # 키(상품)이 중복되는지는 확인하여 수량을 더한다.
    sd = obj.sale_data
    for _ in range(len(sd)):
        name, count = sd[_][0], sd[_][1]
        if name in _sale_data:
            count = _sale_data[name] + count
        _sale_data[name] = count


# csv 형식으로 저장한다.
def sale_data_to_csv(date):
    base_dir = './data/'
    path = os.path.join(base_dir, '{}'.format(date[:4]))
    # 디렉토리 생성
    Path(path).mkdir(parents=True, exist_ok=True)
    # 경로를 포함한 파일명 지정
    file = '{0}/fruit_{1}_{2}.csv'.format(path, date[:4], date[4:])

    data = "Name, Sales Rate\n"
    for k, v in _sale_data.items():
        data += "{0}, {1}\n".format(k, v)
    fileext.create_file(file, data)


if __name__ == "__main__":
    """
    모듈 테스트
    """
    date = '202007'
    # 2020년 7월 판매자료 파일목록을 구한다.
    _dir = os.path.join(os.getcwd(), 'sample', date)
    get_dir_files(_dir)  # 모듈 사용시 클로저
    # 7월 월간판매량을 구한다.
    for _ in _file_list:
        get_monthly_sale_data(_)
    print(_sale_data)
    sale_data_to_csv(date)
