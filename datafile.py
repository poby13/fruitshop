"""
판매 데이터가 있는 파일 객체
파일 정보를 가진다.
파일을 읽어 온다.
파일을 2차원 튜풀로 만들어 반환한다.
"""
from actlib.file.file import getlineval

class SaleData:
    def __init__(self, file):
        self.file = file

    def getsitename(self):
        print(file(path, 1))

    def getData(self):
        pass





if __name__ == '__main__':
    path = 'source/202007/05/gangnam.txt'
    data = SaleData(path)
    data.getsitename()
