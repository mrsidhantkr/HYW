import cv2
import os

# Directory to store known faces
KNOWN_FACES_DIR = 'known_faces'

def enroll_face(name):
    """Capture and save a new face for enrollment."""
    if not os.path.exists(KNOWN_FACES_DIR):
        os.makedirs(KNOWN_FACES_DIR)

    video_capture = cv2.VideoCapture(0)
    print("Capturing face. Look at the camera...")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error accessing camera.")
            continue

        # Display the captured frame
        cv2.imshow("Face Enrollment", frame)

        # Press 'c' to capture and save the face
        if cv2.waitKey(1) & 0xFF == ord('c'):
            file_path = os.path.join(KNOWN_FACES_DIR, f"{name}.jpg")
            cv2.imwrite(file_path, frame)
            print(f"Face captured and saved as {file_path}")
            break

        # Press 'q' to quit without saving
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Enrollment canceled.")
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    name = input("Enter the name for the new face: ").strip()
    if name:
        enroll_face(name)
    else:
        print("Invalid name. Exiting...")
