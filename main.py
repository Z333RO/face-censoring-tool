# pip install opencv-python
import cv2

video = cv2.VideoCapture('video_sample.mp4')
success, frame = video.read()
height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')

output = cv2.VideoWriter('output_censored.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))
# output = cv2.VideoWriter('output_censored.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# You will see numbers cascading down, those are the frames that the script is working on. When it stops, the script has completed.
# The sample video will take about 1-2 minutes to process.
frame_count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50, 50))
    output.write(frame)
    success, frame = video.read()
    frame_count += 1
    print(frame_count)

output.release()