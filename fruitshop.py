import os
import datafile


if __name__ == '__main__':
    # 파일 목록을 생성한다.
    target = os.path.join(os.getcwd(), 'sample', '202007')
    # 클로저
    datafile.get_dir_files(target)
    print(datafile.file_list)
