import cv2
import numpy as np
import pyautogui

while True:
    screenshot = pyautogui.screenshot(region=(100, 100, 1200, 1200))
    image = np.array(screenshot)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 이미지를 화면에 표시합니다
    cv2.imshow('실시간 화면 캡처', image)

    # ESC 키가 눌리면 루프를 종료합니다
    if cv2.waitKey(1) == 27:
        break

# 모든 OpenCV 창을 닫습니다
cv2.destroyAllWindows()
