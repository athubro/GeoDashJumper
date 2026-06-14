import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(0)
pose = mp.solutions.pose.Pose()

prev = 0
th = 0.1

while True:
    ok, f = cap.read()
    if not ok: 
        break
        print("broken frame")

    f = cv2.flip(f, 1)
    r = pose.process(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))

    if r.pose_landmarks:
        left = r.pose_landmarks.landmark[23].y
        right = r.pose_landmarks.landmark[24].y
        y = (left + right) / 2

        if prev != 0 and (prev - y) > th:
            pyautogui.keyDown("space")
            time.sleep(0.02)
            pyautogui.keyUp("space")
            print("Jump")

        prev = y

    cv2.imshow("cam", f)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
