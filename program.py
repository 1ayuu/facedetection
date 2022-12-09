import face_recognition
import cv2
import numpy as np 
import csv
import os
from datetime import datetime
video_capture-cv2.videocapture(0)
jobs_image=face_recognition.load_image_file("photos/jobs.jpg")
jobs_encoding=face_recognition.face_encoding(jobs_image)[0]

ratantata_image=face_recognition.load_image_file("photos/ratantata.jpg")
ratantata_encoding=face_recognition.face_encoding(ratantata_image)[0]

sadmona_image=face_recognition.load_image_file("photos/sadmona.jpg")
sadmona_encoding=face_recognition.face_encoding(sadmona_image)[0]

tesla_image=face_recognition.load_image_file("photos/tesla.jpg")
tesla_encoding=face_recognition.face_encoding(tesla_image)[0]

know_face_encoding=[
                
                jobs_encoding,
                ratantata_encoding,
                sadmona_encoding,
                tesla_encoding
                ]
know_face_names=[

                    "jobs",
                    "ratantata",
                    "sadmona",
                    "tesla"
                ]
students=know_face_names.copy()
face_locations=[]
face_encodings=[]
face_names=[]
s=True
now =datetime.now()
current_date=now.strftime(" %y - %m - %d ")
f=open(current_date + '.csv','w+',newline ='')
lnwriter=csv.writer(f)
writeTrue : frame=video_capture.read()
small_frame = cv2.resize(frame, [0,0],fx=0.25 ,fy=0.25)
rgb_small_frame=small_frame[:,:,::1]

if s:
                    face_locations=face_recognition.face_locations(rgb_small_frame)
                    face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)

                    face_names=[]
                    for face_encoding in face_encodings:
                        matches=face_recognition.compare_faces(know_face_encoding,face_encoding)
                        name=""
                        face_distance=face_recognition.face_distance(know_face_encoding,face_encoding) 
                        best_match_index=np.argmin(face_distance)
                        if matches[best_match_index]:
                            name=know_faces_names[best_match_index]


                            faces.names.append(name)
                            if name in known_faces_names:
                                if name in students:
                                    students.remove(name)
                                    print (students)
                                    current_time=now.stretime("%H - %M -%S")
                                    lnwriter.writerow([name,current_time])
                                    cv2.imshow("attendence system ",frame)
                                    if cv2.waitkey(1)&0XFF = ord('a'): break

video_capture.release()
cv2.destroyAIWindow()
f.close()                    