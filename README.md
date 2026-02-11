**Project Overview**

This project is an automated attendance system developed using Python and face recognition technology. It detects and recognizes faces in real-time using a webcam and automatically records attendance. The system also includes a timer-based feature that prevents duplicate attendance within 40 minutes.

**Features**

    Real-time face detection and recognition

    Automatic attendance marking

    Timer-based attendance control (40-minute gap)

    Attendance stored in Excel file

    Unknown face detection

    Simple and efficient attendance tracking

**Technologies Used**

    Python

    OpenCV

    Face Recognition Library

    NumPy

    OpenPyXL

    DateTime & Time Module

**Project Structure**

    SmartAttendanceSystem/
    │
    ├── known_faces/        # Store known person images
    ├── attendance.xlsx     # Attendance record file
    ├── main.py             # Main project file

**Installation & Setup**

  1️.Clone the Repository:  
    git clone https://github.com/KarishmaBeniwal/AI-Based-Face-Attendance-with-Timer.git
   
   2️.Install Required Libraries
            
             pip install opencv-python
             pip install face-recognition
             pip install numpy
             pip install openpyxl

**How to Run the Project**

    Add images of known persons inside known_faces folder
    
    (Image name should be the person's name)

    Run the Python file:

    python main.py

    Webcam will start automatically

    Attendance will be recorded in attendance.xlsx

    Press Q to exit the program

**Timer Logic**

    Attendance cannot be marked again for the same person within 40 minutes

    Helps prevent duplicate attendance entries

**Output**

    Attendance is saved in Excel file with:

    Name

    Date

    Time

**Future Improvements**

    GUI Interface

    Database Integration

    Cloud Storage

    Mobile App Integration

    Multiple Camera Support

**Author**

    Karishma Beniwal
    MCA Student | Python Developer | Data Analytics Enthusiast
