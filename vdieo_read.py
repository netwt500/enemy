import cv2
from find_enemy_func import *

count = 1

appear = [0, 0, 0]
intervel = 50
frame_counter = 1

# 동영상 파일 경로
video_path = '/Users/hanjeonghyeon/Desktop/open_sw/sub_lol_project/lol_vdieo.mp4'

# 동영상 파일 열기
cap = cv2.VideoCapture(video_path)

# 동영상이 정상적으로 열렸는지 확인
if not cap.isOpened():
    print("Error: 동영상 파일을 열 수 없습니다.")

else:
    # 동영상이 열렸다면 프레임을 읽어 화면에 표시
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: 프레임을 읽을 수 없습니다.")
            break


        cv2.imshow("main_image", frame)
        # 프레임 저장 (예: frame_0.jpg, frame_1.jpg ...)
        frame_filename = f'save_image/frame_{frame_counter}.jpg'
        cv2.imwrite(frame_filename, frame)
        frame_counter += 1
        image = frame


        #show_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        extract = extract_red(image)

        gray = cv2.cvtColor(extract, cv2.COLOR_BGR2GRAY)

        Dilated_img = invertAndDilate(gray)

        cons = find_Contours(Dilated_img)

        labeled_img, OUTPUT = contours(extract, cons)

        # 메인 이미지 픽셀값 단. 정사각형이여야 작동이 잘됨 **수정 해야 할 것 중에 제일 중요함**
        x2 = 500
        y2 = 500

        # 프레임을 화면에 표시
        #직사각형으로 수정 해야함
        if appear[0] > 0 and 0 in OUTPUT:
            appear[0] = intervel
        elif appear[0] > 0 and 0 not in OUTPUT:
            appear[0] -= 1
            print(0 not in OUTPUT)
        elif appear[0] <= 0 and 0 in OUTPUT:
            appear[0] = intervel
            print("0 등장", appear[0])

        if appear[1] > 0 and 1 in OUTPUT:
            appear[1] = intervel
        elif appear[1] > 0 and 1 not in OUTPUT:
            appear[1] -= 1
        elif appear[1] <= 1 and 1 in OUTPUT:

            print("1 등장", appear[1])
            appear[1] = intervel

        if appear[2] > 0 and 2 in OUTPUT:
            appear[2] = intervel
        elif appear[2] > 0 and 2 not in OUTPUT:
            appear[2] -= 1
        elif appear[2] <= 0 and 2 in OUTPUT:
            print("2 등장", appear[2])
            appear[2] = intervel



        cv2.imshow('Frame', labeled_img)





        # 'q' 키를 누르면 루프 종료
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# 작업 완료 후 자원 해제
cap.release()
cv2.destroyAllWindows()