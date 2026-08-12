import subprocess
from time import sleep
from lcd_i2c import LCD_I2C


def is_pipedal_running():
    result = subprocess.run(
        ["systemctl", "is-active", "pipedald"],
        capture_output=True,
        text=True,
        check=False,
    )

    return result.stdout.strip() == "active"


lcd = LCD_I2C(0x27, 16, 2)

lcd.backlight.on()
lcd.clear()

lcd.write_text("Booting...")

while True:
    if is_pipedal_running():
        break

    sleep(1)

lcd.clear()
lcd.write_text("MAGNUS OPUS 3000")
