#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 0
while x < 10:
    x = x + 1
    if x < 3:
        continue
    print(x)
    if x > 7:
        break


# while 조건:
#     반복실행코드
#     continue      # while 구문 처음으로 가서 계속 실행
#     ...
#     break         # while 구문 탈출



print('----------------------------')

x = 1
total = 0
while 1:                    # 프로그래밍 언어에서 1은 참(True), 0은 거짓(False)
    total = total + x
    if total > 10:
        print(x)
        print(total)
        break
    x = x + 1               # x 값과 total 값을 예상합니다. 