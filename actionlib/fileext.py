"""
텍스트 파일 관련 기능 확장
"""
import os


def get_nth_line(file, nth):
    """
    파일의 지정된 행에 값을 반환다.
    2020.08.23 actionshin@gmail.com
    :param file: 파일의 경로
    :param nth: 행번호
    :return: 읽은 행
    """
    try:
        with open(file, 'r') as f:
            line = f.readlines()[nth - 1:nth][0]
            line = line.split('\n')[0]
            return line
    except (FileNotFoundError, IsADirectoryError) as err:
        # logging.info("{}파일명이나 경로를 다시 확인하세요.".format(file))
        return

# TODO 디렉토리가 없는 경우 생성 추 파일을 저장하도록 수정 - 다형성 이용
def create_file(file, data):
    """
    데이터를 파일에 작성하고 지정된 디렉토리에 파일을 생성한다.
    :param file: (디렉토리/)파일명.txt
    :param data: 파일에 기록할 내용
    :return:
    """

    # 같은 파일이 이미 있으면 (숫자)로 파일명을 변경하여 추가한다. sample(1).txt
    n = 1
    while os.path.isfile(file):
        n += 1
        index = file.index('.txt')
        if n > 2:
            idx2 = file.index('(')
            file = '{0}({1}){2}'.format(file[:idx2], n, file[index:])
        else:
            file = '{0}({1}){2}'.format(file[:index], n, file[index:])

    with open(file, 'w') as f:
        f.write(data)
