import cv2

frameWidth = 640
frameHeight = 480
minArea = 500
faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0
while True:
	success, img = cap.read()
	imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

	for (x, y, w, h) in faces:
		area = w*h
		if area > minArea:
			cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
			cv2.putText(img, "Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)

			imgRoi = img[y:y+h, x:x+w]
			cv2.imshow("ROI", imgRoi)


	cv2.imshow("Result", img)
	if cv2.waitKey(1) & 0xFF == ord('s'):
		cv2.imwrite("Saved_Images/face_" + str(count) + ".jpg", imgRoi)
		cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
		cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
		cv2.imshow("Result", img)
		cv2.waitKey(500)
		count += 1

	elif cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()



# img = cv2.imread('Resources/lena.png')
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# for (x, y, w, h) in faces:
# 	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2.imshow("Result", img)
