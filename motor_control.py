import RPi.GPIO as GPIO
import time

# Motor GPIO Pins
MOTOR_PIN1 = 24
MOTOR_PIN2 = 23
ENABLE_PIN = 25

pwm = None  # Global PWM instance


def setup_motor():
    """Setup motor GPIO pins and PWM."""
    global pwm
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTOR_PIN1, GPIO.OUT)
    GPIO.setup(MOTOR_PIN2, GPIO.OUT)
    GPIO.setup(ENABLE_PIN, GPIO.OUT)

    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)

    pwm = GPIO.PWM(ENABLE_PIN, 1000)  # 1kHz frequency
    pwm.start(100)  # Full speed


def unlock_door():
    """Run motor for 5 seconds to simulate unlocking the door."""
    print("Unlocking door...")
    GPIO.output(MOTOR_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    time.sleep(5)
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    print("Door unlocked!")


def cleanup_motor():
    """Clean up motor GPIO settings."""
    if pwm:
        pwm.stop()
    GPIO.cleanup()
