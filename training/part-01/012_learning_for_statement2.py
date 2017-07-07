#!/usr/bin/env python
# -*- coding: utf-8 -*-

scope = [1, 2, 3, 4, 5]

# 아래 라인에 에러가 있습니다. 수정하세요.(힌트: 인덴트 중요성)
 for x in scope:    
    print(x)

    if x < 3:
        continue    # 다음 반복문 수행, continue 이후 코드는 실행하지 않음
        print("Hello.")

# 아래 라인에 에러가 있습니다. 수정하세요.(힌트: 인덴트 중요성)
        else:       
        break       # for 반목문을 탈출
