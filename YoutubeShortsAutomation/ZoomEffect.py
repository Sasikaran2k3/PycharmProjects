import cv2
vidcap = cv2.VideoCapture('Data/0.mp4')
success,image = vidcap.read()
count = 0
print("I am in success")
while success:
  success,image = vidcap.read()
  print(image)
  resize = cv2.resize(image, (640, 480), interpolation = cv2.INTER_LINEAR)
  cv2.imwrite("%03d.jpg" % count, resize)
  if cv2.waitKey(10) == 27:
      break
  count += 1