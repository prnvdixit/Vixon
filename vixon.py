import numpy as np
import cv2
import requests

cap = cv2.VideoCapture(0)

url = "http://192.168.43.1:8080/shot.jpg"

while(True):
    
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    ## **Your Code Goes Here** ##	
    
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
