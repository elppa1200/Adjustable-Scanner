import cv2, os
import numpy as np

img_path = 'image/5828706_4855516_1.jpg'
filename, ext = os.path.splitext(os.path.basename(img_path))
ori_img = cv2.imread(img_path)

img = ori_img.copy()

src = []

errorprint2 = np.zeros((200,850,3),np.uint8)
errorprint3 = np.zeros((200,850,3),np.uint8)
errorprint4 = np.zeros((200,850,3),np.uint8)

def mouse_handler(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONUP:
  
    src.append([x, y])
    
    for xx, yy in src:
      cv2.circle(img, center=(xx, yy), radius=2, color=(0, 255, 255), thickness=-1, lineType=cv2.LINE_AA)      

    cv2.imshow('img', img)

    if len(src) == 2:
      if src[0][0] > src [1][0]:
        cv2.putText(errorprint2, 'wrong point! replace first and second x position', (30,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Error',errorprint2)
        cv2.destroyWindow("img")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    if len(src) == 3:
      if src[1][1] > src[2][1]:
        cv2.putText(errorprint3, 'wrong point! replace second and third y position', (30,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Error',errorprint3)
        cv2.destroyWindow("img")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

    if len(src) == 4:
      
      if src[2][0]<src[3][0]:
        cv2.putText(errorprint4, 'wrong point! replace third and fourth x position', (30,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Error',errorprint4)
        cv2.destroyWindow("img")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
      
      
      else:
        src_np = np.array(src, dtype=np.float32)

        width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
        height = max(np.linalg.norm(src_np[0] - src_np[3] ), np.linalg.norm(src_np[1] - src_np[2]))


        dst_np = np.array([
          [0, 0],
          [width, 0],
          [width, height],
          [0, height]
        ], dtype=np.float32)

        M = cv2.getPerspectiveTransform(src=src_np, dst=dst_np)
        result = cv2.warpPerspective(ori_img, M=M, dsize=(width, height))

        cv2.imshow('result', result)
        cv2.imwrite('result/%s_result%s' % (filename, ext), result)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img', ori_img)
cv2.waitKey(0)
