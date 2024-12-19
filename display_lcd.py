from RPLCD.i2c import CharLCD
import time

# Initialize I2C LCD
lcd = CharLCD('PCF8574', 0x27)  # Change 0x27 to your LCD I2C address if needed.

def display_message(message, duration=3):
    """Display a message on the LCD for a set duration."""
    lcd.clear()
    lcd.write_string(message)
    time.sleep(duration)
    lcd.clear()
