import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(0)


prev = 0
th = 0.1

while True:
    ok, f = cap.read()
    if not ok: 
        break
        print("frame issue")

    f = cv2.flip(f, 1)
    r = mp.solutions.pose.Pose().pose.process(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))

    if r.pose_landmarks:
        left = r.pose_landmarks.landmark[23].y
        right = r.pose_landmarks.landmark[24].y
        finger = r.pose_landmarks.landmark[16]
        
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