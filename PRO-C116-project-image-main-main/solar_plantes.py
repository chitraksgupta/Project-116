import cv2

img = cv2.imread("solar-system.jpg")

cv2.imshow("output",img) 
cv2.waitKey(0)

cv2.putText(img,
            "sun"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "mercury"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "mars"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "earth"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "venus"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "jupiter"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "saturn"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "pluto"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.putText(img,
            "neptune"
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0,5,
            (255,255,255)
            )

cv2.imwrite("Solaro_systemwithname.jpg",img)