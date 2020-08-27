"""
텍스트 파일 관련 기능 확장
"""


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
