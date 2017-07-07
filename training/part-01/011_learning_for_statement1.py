#!/usr/bin/env python
# -*- coding: utf-8 -*-

scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)

# for 변수 in 범위:
#   반복으로 실행할 코드
# 
# for문의 범위로 사용된 자료형은 시퀀스 자료형 또는 반복 가능한 자료형
# 문자열, 리스트, 튜플, 사전, range(), 그외 반복 가능한 객체

print('-------------------------')

# 문자열
str = 'abcdef'
for s in str:
    print(s)

print('-------------------------')

# 리스트
list = [1, 2, 3, 4, 5]
for l in list:
    print(l)

print('-------------------------')
# 사전
ascii_codes = {'a':97, 'b':98, 'c':99}
for a in ascii_codes:
    print(a)

print('-------------------------')
# range()
for v in range(10):
    print(v)
