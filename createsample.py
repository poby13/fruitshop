#!/usr/bin/python3
"""
'과일가게'는 각 지점에서 하루 2회 판매량을 텍스트 파일로 전달한
전달 받는 샘플 텍스트 파일을 자동으로 sample 폴더에 생성
파일은 '년월' 디렉토리에 '날짜' 폴더를 만들어 판매현황 파일이 추가

$ python createsample.py


pathlib :: https://docs.python.org/3/library/pathlib.html
디렉토리 생성을 위해 표준 라이브러리인 pathlib를 사용
비어있는 디렉토리 삭제를 위해 표준 라이브러리 shutil을 사용
이 모듈은 서로 다른 운영 체제에 적합한 형태의 파일 시스템 경로를 나타내는 클래스가 제공


명명규칙 ::
함수 - '동작_대상', 모두 소문자, 두개의 단어는 '_'로 구분


author  actionshin@gmail.com
version 1.0, 20/08/12
since   python3.5
"""

import os
import shutil
from pathlib import Path
from random import randint
from actionlib import fileext


def create_sale_data():
    """
    판매상품,판매량의 형식으로 판매데이터 샘플을 만든다.
    판매상품의 이름은 알파벳을 사용한다.
    판매데이터 예)'a,4,b,7,d,3,h,8,k,9,a,10'
    :return: [문자열]판매데이터
    """
    # 판매 횟수를 (최소, 최대)로 설정
    sales_count = (5, 25)
    # 판매상품명은 a부터 시작
    # 판매상품 종류 (시작, 끝)으로 설정, a(97)부터 z(122)
    sale_name = (97, 106)
    # 1회 판매 갯수
    sale_count = (1, 5)
    # for문으로 문자열을 만들어 나가려면 for문 밖에 변수가 있어야 한다.
    result = ''
    for sc in range(randint(sales_count[0], sales_count[1])):
        # 상품명과 갯수는 콤마로 구분하며, 처음에는 콤마를 넣지 않는다.
        s = ','
        if not result:
            s = ''
        # 상품을 지정하는 숫자 chr(97)부터 chr(122)는 'a'부터 'z'을 표현
        # 판매건수는 1부터 10개까지
        result += '{0}{1},{2}'.format(s, chr(randint(sale_name[0], sale_name[1])),
                                      randint(sale_count[0], sale_count[1]))
    return result




def do_init():
    """
    샘플 코드를 생성하기 위해 필요한 점포명과 판매량을 기록할 날짜를 정하고
    sample 폴더에 파일을 월별로 생성한다.
    점포명과 판매일을 정한다. 점포명은 파일명이 된다.
    년월 디렉토리에 날짜 폴더를 만든다.

    :return:
    """
    branches = ('gangnam', 'songpa', 'nowon', 'incheon', 'suwon')
    dates = ('20200705', '20200706', '20200709', '20200811', '20200812')

    # 현재 경로에 있는 sample폴더에 '년월\날짜' 디렉토리 만들기
    base_dir = './sample/'

    # sample 폴더가 있는 경우 계속할지 확인
    try:
        if os.path.isdir(base_dir):
            print("""
폴더가 이미 있습니다.
sample 폴더를 지우고 새로 만드시려면 ... y
기존 폴더에 샘플을 추가하려면 ... a
작업을 취소하려면 ... n
            """)
            is_folder_exists = input("계속하시겠습니까? 키를 입력하고 엔터 ... (y, a, [n])")
            if is_folder_exists == 'n':
                print("샘플파일 작업이 취소되었습니다.")
                return
            elif is_folder_exists == 'y':
                print("sample 폴더를 삭제합니다.")
                # rmdir은 비어있지 않은 디렉토리를 삭제하지 못함.
                # os.rmdir(base_dir)
                shutil.rmtree(base_dir, ignore_errors=True)
                print("sample 폴더를 생성하고 샘플데이터를 추가합니다.")
            elif is_folder_exists == 'a':
                print("기존 sample 폴더에 데이터를 추가합니다.")
            else:
                print("입력값이 잘 못 입력되었습니다.")
                return
    except NameError as e:
        pass

    for date in dates:
        path = os.path.join(base_dir, '{0}/{1}'.format(date[:6], date[6:]))

        # 디렉토리 생성
        Path(path).mkdir(parents=True, exist_ok=True)

        # 지점별 판매 샘플 파일 만들기
        for branch in branches:
            text = '{0}_{1}_{2}\n'.format(branch, '#fruitshop#', date)
            text += create_sale_data()
            file = '{0}/{1}.txt'.format(path, branch)
            fileext.create_file(file, text)


if __name__ == '__main__':
    # 샘플파일 작업 시작
    do_init()
