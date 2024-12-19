import face_recognition
import cv2
import os

# Path to known faces directory
KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6  # Face recognition tolerance (lower = stricter)

def load_known_faces():
    """Load known faces and their encodings from a directory."""
    known_encodings = []
    known_names = []

    for filename in os.listdir(KNOWN_FACES_DIR):
        image_path = os.path.join(KNOWN_FACES_DIR, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]  # Get face encoding
        known_encodings.append(encoding)
        known_names.append(os.path.splitext(filename)[0])  # Name is the file name
    return known_encodings, known_names

def recognize_faces(known_encodings, known_names):
    """Use webcam to recognize faces."""
    print("Initializing camera...")
    video_capture = cv2.VideoCapture(0)  # Open webcam

    while True:
        ret, frame = video_capture.read()  # Capture frame-by-frame
        if not ret:
            continue

        # Detect faces
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding, TOLERANCE)
            name = "Unknown"

            if True in matches:
                match_index = matches.index(True)
                name = known_names[match_index]

            print(f"Detected: {name}")
            if name != "Unknown":
                video_capture.release()
                return True  # Face recognized successfully

        cv2.imshow("Face Recognition", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return False  # No face recognized
