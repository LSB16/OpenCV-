import numpy as np
import cv2

src = cv2.imread('./source/dog.bmp')

if src is None: raise Exception('Image load failed')

rc = cv2.selectROI(src, True, False)                                        # 마우스 드래그로 roi 영역을 설정
print(rc)

mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 1, cv2.GC_INIT_WITH_RECT)            # mask 값이 변경된다.

mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype(np.uint8)

dst = src * mask2[:,:,np.newaxis]                                           # src는 컬러 영상이므로 차원을 맞춰줌

cv2.imshow('dst', dst)
cv2. waitKey()
cv2.destroyAllWindows()