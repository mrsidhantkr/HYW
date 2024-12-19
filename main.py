from motor_control import setup_motor, unlock_door, cleanup_motor
from display_lcd import display_message
from face_recognition_handler import load_known_faces, recognize_faces
from fingerprint_handler import initialize_sensor, verify_fingerprint

def main():
    try:
        # Setup motor
        setup_motor()

        # Initialize fingerprint sensor
        sensor = initialize_sensor()
        if not sensor:
            print("Fingerprint sensor not initialized. Exiting...")
            return

        # Load known faces
        known_encodings, known_names = load_known_faces()
        print("Known faces loaded. Ready for face recognition...")

        # Face Recognition
        display_message("Scan Face")
        face_success = recognize_faces(known_encodings, known_names)

        if face_success:
            print("Face recognized. Unlocking door...")
            display_message("Face Recognized!")
            unlock_door()
            display_message("Door Opened")
        else:
            print("Face not recognized. Switching to fingerprint...")
            display_message("Switching to Fingerprint")

            # Fingerprint Verification
            fingerprint_success = verify_fingerprint(sensor)
            if fingerprint_success:
                print("Fingerprint verified. Unlocking door...")
                display_message("Fingerprint OK!")
                unlock_door()
                display_message("Door Opened")
            else:
                print("Fingerprint not recognized. Access denied.")
                display_message("Access Denied")

    except KeyboardInterrupt:
        print("Program interrupted.")
    finally:
        cleanup_motor()
        print("Program ended. Resources cleaned up.")

if __name__ == "__main__":
    main()
