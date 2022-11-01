'''
Python 6 nodarbības mājasdarbs Nr.3

Uzdevums: aizpildīt vietas ar atzīmi TODO
'''

import numpy as np
import cv2

# importēt "python.jpg" bildi
img = cv2.imread("python.jpg")
cv2.imshow("Regular image",img)
cv2.waitKey(0)

# Pārveidot bildi melnbaltu un izvadīt uz ekrāna
img_melnbalts = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Black and White image",img_melnbalts)
cv2.waitKey(0)

# pielietot Caddy edge detection uz originālās bildes un izvadīt uz ekrāna
img_caddy = cv2.Canny(image=img, threshold1=100, threshold2=200)
cv2.imshow("Caddy image",img_caddy)
cv2.waitKey(0)

# Pārveidot zilo krāsu par sarkanu un izvadīt uz ekrāna
img_zils_sarkans = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Blue to Red image",img_zils_sarkans)
cv2.waitKey(0)

cv2.destroyAllWindows()