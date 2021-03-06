﻿# pip install xlsxwriter
from xlsxwriter import Workbook
# 엑셀 파일을 건드리자
# 다른 엑셀 write 라이브러리인 pyexcelerate보다 느리긴 하지만 문서가 굉장히 잘 되어 있다
# xlwt도 이것보다 빠르긴 하지만 .xlsx 지원을 안하니 제끼자

wb = Workbook('Test.xlsx')
# Workbook 클래스의 인스턴스를 받아야 함
# 파일 이름 옵션을 넘겨줄 수 있음

sheet = wb.add_worksheet('Test sheet')
# 시트를 추가해야 함

data = [
    (1, 'a'),
    (2, 'b'),
    (3, 'c')
]
# write를 위한 데이터

for idx, (left, right) in enumerate(data):
    # row를 판단하기 위한 enumerate

    sheet.write(idx, 0, left)
    sheet.write(idx, 1, right)
    # write(row, column, data)

data = ['a', 'b', 'c']
sheet.write_row('A4', data)
# row에 일렬로 데이터 삽입

sheet.write_column('E1', data)
# column에 일렬로 데이터 삽입

wb.close()
