import cv2
import imutils
import numpy as np
import pytesseract

def process_frame(frame):
    # Resize the frame
    frame = cv2.resize(frame, (620, 480))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Bilateral filtering
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # Edge detection
    edged = cv2.Canny(gray, 30, 200)

    # Find contours
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    screenCnt = None

    # Loop over contours
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    if screenCnt is not None:
        cv2.drawContours(frame, [screenCnt], -1, (0, 255, 0), 3)

        # Masking
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1)
        new_image = cv2.bitwise_and(frame, frame, mask=mask)

        # Cropping
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

        # Read the number plate
        text = pytesseract.image_to_string(cropped, config='--psm 11')
        print("Detected Number is:", text)

    cv2.imshow('Live Video', frame)

# Specify the index of your USB camera (e.g., 0, 1, 2, ...)
usb_camera_index = 0
cap = cv2.VideoCapture(usb_camera_index)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    process_frame(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
