import cv2

path = '../../Learning_OpenCV_3_Computer_Vision_with_Python_Second_Edition_Code/Chapter_8_Code/movie.mpg'
new_path = 'picture/MyOutputVid.avi'
#cv2.namedWindow('my window', cv2.WINDOW_FREERATIO)
videoCapture = cv2.VideoCapture(0)
#fps = videoCapture.get(cv2.CAP_PROP_FPS)
fps = 30
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(new_path, cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

#success为是否成功获取帧，frame为读取到的图像
success, frame = videoCapture.read()
numFramesRemaining = 10*fps - 1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    #cv2.imshow('my window', frame)
    success, frame = videoCapture.read()
    numFramesRemaining -= 1
videoCapture.release()