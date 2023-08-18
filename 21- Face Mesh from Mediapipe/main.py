import cv2
import mediapipe as mp

detector = mp.solutions.face_mesh.FaceMesh()
cap = cv2.VideoCapture(0)

while True :
    _ ,frame = cap.read()
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = detector.process(rgb_frame)
    height,width,_ = frame.shape
    
    try:
        for facial_landmark in results.multi_face_landmarks:
         for i in range (0,468):
            pt = facial_landmark.landmark[i]
            x = int(pt.x * width)
            y = int(pt.y * height)
        
            cv2.circle(frame,(x,y),2,(0,255,255),-1)

    except Exception as e:
     print("An exception occurred: ", e) 
    
    cv2.imshow('Frame',frame)
    if cv2.waitKey(27) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()    
    