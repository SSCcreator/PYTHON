import cv2
import numpy as np

print(np.__version__)

# cap = cv2.VideoCapture("rtsp://admin:a1234567890@10.246.162.40:554")
# cap = cv2.VideoCapture('output.avi')
try:
    cap = cv2.VideoCapture(1)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # cap = cv2.VideoCapture("rtsp://admin:c@m4UCab@10.246.162.202:554")
    cv2.namedWindow('A12', cv2.WINDOW_NORMAL)
    # cv2.namedWindow('A1')
    # cap.set(3, 1920)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    # cap.set(4, 1080)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    # cap.set(5, 160)

    print(width, height, fps)
    # fourcc = cv2.VideoWriter_fourcc(*'H264'*'MJPG')
    # out = cv2.VideoWriter('outputA21.avi', cv2.VideoWriter_fourcc(    *'MJPG'), 160, (width, height))
    while True:
        ret, frame = cap.read()
        # cv2.rotate(frame, cv2.ROTATE_180)
    # frame = cv2.resize(frame, (0, 0), fx=0.75, fy=0.75)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # out.write(frame)
    # fps = int(cap.get(5))
    # print("Частота кадров: ", fps, "кадров в секунду")
    # Получить количество кадров
    # frame_count = cap.get(7)
    # print("Количество кадров: ", frame_count)
        cv2.imshow('A12', frame)
        # Инициализировать объект записи видео
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), cap.get(4), cap.get(5))


except cv2.error:
    print('Камера не найдена.')
