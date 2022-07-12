# cv2.grabcut 함수 테스트 
---
그랩컷은 2가지 방법으로 수행할 수있다.

1. 객체의 위치를 사각형 형태로 입력
2. 객체 부분과 배경 부분을 마우스로 지정해서 입력

이번 테스트는 1번 방법에 대한 코드이다.

+ cv2.selectROI(arg1, arg2, arg3, arg4)
  - arg1(winname): 윈도우 창 이름
  - arg2(img): 윈도우 창에 표시할 이미지
  - arg3(showCrossHair=True): 선택 영역 중심에 십자 모양 표시 여부
  - arg4(fromCenter=False): 마우스 시작 지점을 영역의 중심으로 지정

+ cv2.grabCut(arg1, arg2, arg3, arg4, arg5, arg6)
  - arg1(img): 입력 영상, 8비트 3채널
  - arg2(mask): 입출력 마스크
  - arg3(bgdModel): 임시 배경 모델 행렬
  - arg4(fgdModel): 임시 전경 모델 행렬
  - arg5(iterCount): 결과 생성을 위한 반복 횟수
  - arg6(mode): cv2.GC_ 로 시작하는 모드 상수

+ np.where(arg1,arg2,arg3)
  - arg1(condition): 조건문
  - arg2(x): 조건문이 True일때 치환할 값
  - arg3(y): 조건문이 False일때 치환할 값

```python
import numpy as np

array1 = np.arange(5,15)
print(array1)                      # [5 6 7 8 9 10 11 12 13 14]
array2 = np.where(array1 > 10)[0]  
print(array2)                      # (array([6, 7, 8, 9], dtype=int64),) 튜플 형식 반환

array2Da = np.array([[15,8,12],[11,7,3]]) 
print(np.where(array2Da > 10, array2Da, 10))    # 10미만 원소는 10으로 치환, 10 이상 원소는 원래 값 유지
'''
[[15 10 12]
 [11 10 10]]
'''
```
