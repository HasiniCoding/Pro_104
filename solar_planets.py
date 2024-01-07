import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img, 
            "Sun",
            (20,300),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))

cv2.putText(img, 
            "Mercury",
            (105,200),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))

cv2.putText(img, 
            "Venus",
            (200,180),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))

cv2.putText(img, 
            "Earth",
            (290,180),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))

cv2.putText(img, 
            "Mars",
            (390,190),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))

cv2.putText(img, 
            "Jupiter",
            (600,80),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))

cv2.putText(img, 
            "Saturn",
            (740,130),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))  
            
cv2.putText(img, 
            "Uranus",
            (940,150),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))    

cv2.putText(img, 
            "Neptune",
            (1080,150),
            fontFace = cv2.FONT_HERSHEY_COMPLEX, 
            fontScale = 0.5, 
            color = (225,225,255))

cv2.imshow("output", img)
cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.waitKey(0)