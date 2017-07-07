#!/usr/bin/env python
# -*- coding: utf-8 -*-

scope = [1, 2, 3]
for x in scope:
    print(x)
    #break
else:
    print("Perfect")

# for 변수 in 범위:
#     반복실행코드
# else:
#     for 구문이 모두 실행되었을 때 실행할 코드

print('--------------------------')

# 위의 코드와 비교 합니다.
for x in scope:
    print(x)
    break
else:
    print("Perfect")