import time
from pyfingerprint.pyfingerprint import PyFingerprint

def enroll_fingerprint(sensor):
    """Enroll a new fingerprint."""
    try:
        print("Waiting for finger to enroll...")

        # Wait for a finger to be placed on the sensor
        while not sensor.readImage():
            pass

        # Convert the image to characteristics and store in CharBuffer1
        sensor.convertImage(0x01)

        # Check if the fingerprint is already enrolled
        result = sensor.searchTemplate()
        position_number = result[0]

        if position_number >= 0:
            print(f"Fingerprint already exists at position {position_number}")
            return

        print("Remove finger...")
        time.sleep(2)

        print("Waiting for the same finger again...")
        # Wait for the same finger to be placed on the sensor
        while not sensor.readImage():
            pass

        # Convert the image to characteristics and store in CharBuffer2
        sensor.convertImage(0x02)

        # Compare the two buffers
        if sensor.compareCharacteristics() == 0:
            raise Exception("Fingers do not match!")

        # Create a template
        sensor.createTemplate()

        # Save the template at a new position
        position_number = sensor.storeTemplate()
        print(f"Fingerprint enrolled successfully at position {position_number}!")

    except Exception as e:
        print(f"Failed to enroll fingerprint: {e}")

if __name__ == "__main__":
    try:
        # Initialize the sensor
        sensor = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)
        if not sensor.verifyPassword():
            raise ValueError("Invalid fingerprint sensor password.")

        print("Fingerprint sensor initialized.")
        enroll_fingerprint(sensor)

    except Exception as e:
        print(f"Error initializing fingerprint sensor: {e}")
