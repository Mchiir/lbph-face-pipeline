# Detect which camera to use (working came, either bult-in or external webcam)
import cv2

for i in range(5):  # test 0–4
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print(f"✅ Camera {i} works!")
        else:
            print(f"⚠️ Camera {i} opened but no frame.")
        cap.release()
    else:
        print(f"❌ Camera {i} not found.")