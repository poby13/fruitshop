import os
import datafile


if __name__ == '__main__':
    # 파일 목록을 생성한다.
    target_path = os.path.join(os.getcwd(), 'sample', '202007')
    datafile.make_monthly_data(target_path)
    print()
