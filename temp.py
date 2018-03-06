import numpy
import cv2
import matplotlib.pyplot as plt
'''
img = cv2.imread("adi.jpg",0)
cv2.imshow('image', img)
cv2.waitKey(0)
plt.imshow(img,cmap='gray')
plt.show()'''
cap = cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    cv2.imshow('Vid',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
m=cv2.imread("ori.png")
med=cv2.medianBlur(m,5)
m1=cv2.medianBlur(m,3)
m2=cv2.medianBlur(m,7)

cv2.imshow('m1', m1)

cv2.imshow('image', m)
#cv2.imshow('med', med)
#cv2.imshow('m2', m2)

cv2.waitKey(0)
#image = cv2.imread("lenna.jpg")
gaussian_3 = cv2.GaussianBlur(m1, (9,9), 10.0)
unsharp_image = cv2.addWeighted(m1, 1.5, gaussian_3, -0.5, 0, m1)
#cv2.imwrite("lenna_unsharp.jpg", unsharp_image)

cv2.imshow('usm1', gaussian_3)
cv2.imshow('usm2', unsharp_image)
cv2.waitKey(0)

cv2.destroyAllWindows()