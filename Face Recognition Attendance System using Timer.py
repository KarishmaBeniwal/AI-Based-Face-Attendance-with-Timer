import cv2
import numpy as np
import face_recognition
import os
import openpyxl
from openpyxl import Workbook
from datetime import datetime
import time


KNOWN_FACES_DIR = "known_faces"
ATTENDANCE_FILE = "attendance.xlsx"
ATTENDANCE_GAP = 40 * 60   # 40 minutes (in seconds)



# Dictionary to store last attendance time
attendance_timer = {}   # { name : last_time }

# Ensure attendance file exists
if not os.path.exists(ATTENDANCE_FILE):
    wb = Workbook()
    ws = wb.active
    ws.append(["Name", "Date", "Time"])
    wb.save(ATTENDANCE_FILE)

# Load known faces
print("Loading known faces...")
known_encodings = []
known_names = []

for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = face_recognition.load_image_file(
            os.path.join(KNOWN_FACES_DIR, filename)
        )
        encoding = face_recognition.face_encodings(image)
        if encoding:
            known_encodings.append(encoding[0])
            known_names.append(os.path.splitext(filename)[0])

print(f"Loaded {len(known_encodings)} known faces.")

# Function to mark attendance with 40 min rule
def mark_attendance(name):
    current_time = time.time()

    # Check cooldown
    if name in attendance_timer:
        if current_time - attendance_timer[name] < ATTENDANCE_GAP:
            return  # 40 min not completed

    # Mark attendance
    now = datetime.now()
    date_string = now.strftime('%Y-%m-%d')
    time_string = now.strftime('%H:%M:%S')

    wb = openpyxl.load_workbook(ATTENDANCE_FILE)
    ws = wb.active
    ws.append([name, date_string, time_string])
    wb.save(ATTENDANCE_FILE)

    attendance_timer[name] = current_time
    print(f"Attendance marked for {name}")

# Start webcam
video_capture = cv2.VideoCapture(0)
print("Starting webcam...")

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        name = "Unknown"

        if known_encodings:
            distances = face_recognition.face_distance(
                known_encodings, face_encoding
            )
            best_match_index = np.argmin(distances)

            if distances[best_match_index] < 0.4:
                name = known_names[best_match_index]
                mark_attendance(name)

        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2
        )

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
print("Program stopped. Attendance saved successfully!")
